# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class BokespiderPipeline(object):
    def __init__(self):
        '''链接MongoDB并创建存储数据库'''
        host = '127.0.0.1'
        port = 27017
        conn = pymongo.MongoClient(host=host,port=port)
        dbname =conn['Boke']
        self.post_info = dbname['text2']

    def process_item(self, item, spider):
        #将数据存入MongoDB中
        for i in range(0,len(item['name'])):
            name=item["name"][i]
            url = item["url"][i]
            hits = item["hits"][i]
            comment = item["comment"][i]
            dict_item = {"name":name,
                         "url":url,
                         "hits":hits,
                         "comment":comment}
            self.post_info.insert(dict_item)

        return item
