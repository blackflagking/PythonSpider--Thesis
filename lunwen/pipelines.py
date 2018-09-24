# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class LunwenPipeline(object):
    # #json文件形式保存
    # def __init__(self):
    #     self.file = codecs.open("C:\\Users\\Administrator\\Desktop\\Thesis.txt", 'wb', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + '\n'
    #     self.file.write(line)
    #     return item
    #
    # def spider_closed(self, spider):
    #     self.file.close()

    def __init__(self):
        filename = "C:\\Users\\Administrator\\Desktop\\Thesis\\跨境物流论文.txt"
        filename = unicode(filename, "utf8")
        self.file = codecs.open(filename, 'a', encoding='utf-8')


    def process_item(self, item, spider):
        # print '$$$$$'
        # print item['tittle']
        # print item['lunwen']
        head = json.dumps(item['tittle'], encoding='utf-8', ensure_ascii=False)
        body = json.dumps(item['lunwen'], encoding='utf-8', ensure_ascii=False)
        # head = item['tittle']
        # body = item['lunwen']
        n = '\t\n\n\t'

        block = head + n + body + n
        self.file.write(block)
        return item

    def spider_closed(self):
        self.file.close()