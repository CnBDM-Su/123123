# -*- coding: UTF-8 -*-
'''
This spider extracts specific content from given movie links which can be 
accessed from Redis Database by redis_key "movie_links" and stores the data
to HBase.
Moreover, this spider should export link to more reviews to Redis Database
as redis_key "more_reviews".
'''

import os
import sys
import scrapy
from scrapy_redis.spiders import RedisSpider
from crawler_gewara.items import CrawlerGewaraItem

reload(sys)
sys.setdefaultencoding('utf-8')

class MovieContentSpider(RedisSpider):
    name = "movieContent"
    redis_key = "movie_links"

    def parse(self, response):
        hashed_images = []
        host = self.settings['REDIS_HOST']
        item = CrawlerGewaraItem()
        title = response.xpath('//h1/text()').extract()[0]
        try:
            director = response.xpath('//div[@class="lineBox clear"]/span/em/text()').extract()
        except IndexError:
            director = ''
        try:
            actor = response.xpath('//span[@class="name"]/text()').extract()[0]
        except Exception:
            actor = ''
        lis = response.xpath('//div[@class="ui_movieInfo_open clear"]/ul/li').extract()
        time = lis[0]
        type = lis[1]
        country = lis[2]
        images_url =  response.xpath('//div[@class="ui_pic mr30"]/img/@src').extract()
        item['url'] = response.url
        item['Title'] = title
        item['Director'] = director
        item['ReleaseTime'] = time
        item['Types'] = type
        item['Country'] = country
        item['Actor'] = actor
        item['image_url'] = images_url
        yield item
