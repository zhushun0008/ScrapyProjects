# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo

class NovelspiderPipeline(object):
    host = settings['MONGODB_HOST']
    port = settings['MONGODB_PORT']
    dbName = settings['MONGODB_DBNAME']
    docName = settings['MONGODB_DOCNAME']

    client = pymongo.MongoClient(host=host, port=port)
    db = client[dbName]
    doc = db[docName]
    def process_item(self, item, spider):
        bookInfo = dict(item)
        self.doc.insert(bookInfo)
        return item
