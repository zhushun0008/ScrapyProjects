# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider
from scrapy import Selector
from novelSpider.items import NovelspiderItem
import scrapy


class NovelspderSpider(scrapy.Spider):
    name = "novelSpder"
    start_urls = (
        'http://www.daomubiji.com//',
    )
    def parse(self, response):
        allBookTable = response.xpath('//table')
        for eachBook in allBookTable:
            bookName = eachBook.xpath('tr[1]/td/center/h2/text()').extract()[0]
            content = eachBook.xpath('tr/td/a/text()').extract()
            urls = eachBook.xpath('tr/td/a/@href').extract()
            for i in xrange(len(urls)):
                item = NovelspiderItem()
                item['bookName'] = bookName
                item['chapterURL'] = urls[i]
                # try可以用于检测错误，出现错误以后就会运行except里面的内容。
                try:
                    item['bookTitle'] = content[i].split(' ')[0]
                    item['chapterNum'] = content[i].split(' ')[1]
                except Exception,e:
                    continue

                try:
                    item['chapterName'] = content[i].split(' ')[2]
                except Exception,e:
                    item['chapterName'] = content[i].split(' ')[1][-3:]
                yield item
