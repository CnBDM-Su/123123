# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerGewaraItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url = scrapy.Field()
    Title = scrapy.Field()
    ReleaseTime = scrapy.Field()
    Types = scrapy.Field()
    Country = scrapy.Field()
    Language = scrapy.Field()
    Director = scrapy.Field()
    Actor = scrapy.Field()
    images = scrapy.Field()
    image_url = scrapy.Field()
    image_paths = scrapy.Field()
    pass
