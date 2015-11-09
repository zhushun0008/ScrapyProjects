# -*- coding: utf-8 -*-
import scrapy
from DouBanMovie.items import DoubanmovieItem

class DoubanmoviespiderSpider(scrapy.Spider):
    name = "DoubanMovieSpider"
    allowed_domains = ["douban.com"]
    start_urls = (
        'http://movie.douban.com/top250',
    )
    myMainUrl = 'http://movie.douban.com/top250'

    def parse(self, response):
        moviesAllInfo = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for tempMovie in moviesAllInfo:
            movieItem = DoubanmovieItem()
            titles = tempMovie.xpath('div/div[2]/div[1]/a/span/text()').extract()
            title = ''
            for tempTitle in titles:
                title += tempTitle

            desc = tempMovie.xpath('div/div[2]/div[2]/p[1]/text()').extract()[0]
            rating = tempMovie.xpath('div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            movieItem['title'] = title
            movieItem['description'] = desc
            movieItem['rating'] = rating
            quote = tempMovie.xpath('div/div[2]/div[2]/p[2]/span/text()').extract()
            if quote:
                movieItem['quote'] = quote
            else:
                movieItem['quote'] = ''
            yield movieItem

        nextLink = response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract()
        if nextLink:
            nextLink = self.myMainUrl + nextLink[0]
            yield scrapy.Request(nextLink, callback=self.parse)


