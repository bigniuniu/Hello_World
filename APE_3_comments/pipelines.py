# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class Ape3CommentsPipeline(object):
    def __init__(self):
        self.f = open("w://python/txt files/白夜追凶.json",'a+',encoding = 'utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii= False)
        self.f.write(str(content)+'\n')
        return item


    def close_spider(self,spider):
        self.f.close()