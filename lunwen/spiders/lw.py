# -*- coding: utf-8 -*-
import scrapy
import sys
from lunwen.items import LunwenItem
import re
import json
# reload(sys)
# sys.setdefaultencoding('utf-8')

class LwSpider(scrapy.Spider):
    name = 'lw'
    allowed_domains = ['www.10ec.cn/zt/data']
    start_urls = ['http://www.100ec.cn/detail--6467881.html']

    def start_requests(self):
        for i in range(1, 5):
            url = 'http://www.100ec.cn/search.html?f=search&terms=%%E8%%B7%%A8%%E5%%A2%%83%%E7%%89%%A9%%E6%%B5%%81&w=zh&p=%s'%i
            yield scrapy.Request(url, callback=self.parse_process, encoding='utf-8')

    def parse_process(self, response):
        item = LunwenItem()
        #a = re.findall('<div>(.*?)<div>', response.body)
        #print response.body.decode('utf-8').encode('gb2312')
        #urls = response.xpath('//div[@class="main_left"]').extract()

        count = response.xpath('//div[@class="search_result"]/dl').extract()
        counts = len(count)

        url = response.xpath('//div[@class="search_result"]')
        urlmsg = url.xpath('dl/dt/a/@href').extract()

        urlnames = []
        for i in range(0,counts):
            i = i + 1
            urlname = url.xpath('dl[%d]/dt/a' % i)
            urlname = urlname.xpath('string(.)').extract()
            print urlname[0]
            urlnames.append(urlname[0])


        print '@@@@@@@@@@@'
        self.out(urlnames, urlmsg)


        for i in range(0, counts):
            # print urlname[i]
            # print '!!!!!!!!!!!!!!!!!!!!!!!!!!!'

            item['url'] = urlmsg[i]
            headtxt = 'http://www.100ec.cn/'
            url = headtxt + item['url']
            print '++++++++++++++++'
            print urlnames[i]
            #item['tittle'] = urlnames[i]
            yield scrapy.Request(url, callback=self.parse, encoding='utf-8', meta={'item': item, 'tittle': urlnames[i]}, dont_filter=True)

    def parse(self, response):
        item = response.meta['item']
        text_pro = response.xpath('//div[@class="detail"]/div[@class="location"]')
        text = text_pro.xpath("//div[@class='main_left']/div[@class='detail']/div[@class='text']")
        txt = text.xpath('string(.)').extract()
        tittle = response.meta['tittle']
        item['lunwen'] = txt
        item['tittle'] = tittle
        yield item



    def out(self, names, msgs):
        for i in names:
            print i
        for i in msgs:
            headtxt = 'http://www.100ec.cn/'
            print headtxt + i
