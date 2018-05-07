'''
This spider crawls iterates index pages and then release movie links 
to Redis Database with redis_key: "movie_links"
'''

import os
import scrapy
from urlparse import urljoin

class GewaraMovieSpider(scrapy.Spider):
    start_urls = ["http://www.gewara.com/movie/searchMovieStore.xhtml?movietype=&order=releasedate&moviestate=&movietime=all&playtype=&searchkey=",]
    name = "movieLinks"
    def parse(self, response):
        host = self.settings['REDIS_HOST']
        lists = []
        initial_lists = response.xpath('//div[@class="title"]/h2/a/@href').extract()
        for li in initial_lists: 
            lists.append(response.urljoin(li))
        for li in lists:
            command = "redis-cli -h " + host + " lpush movie_links " + li
            os.system(command)
        try:
            url = response.urljoin(response.xpath('//a[@class="next"]/@href').extract()[0])
        except:
            return
	yield scrapy.Request(url, callback=self.parse)
