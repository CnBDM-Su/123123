# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.h

from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy import log
from scrapy.pipelines.images import ImagesPipeline

class CrawlerGewaraPipeline(object):
    def process_item(self,item,spider):
        return item

class GewaraImagePipeline(ImagesPipeline):
    default_headers = {
        'accept':'image/webp,image/*,*/*;q=0.8',
        'accept-encoding':'gzip,deflate,sdch,br',
        'accept-language':'zh-CN,zh;q=0.8,en;q=0.6',
        'cookie':'bid=yQdC/AzTaCw',
        'referer':'https://',
        'user-agent':'Mozilla/5.0',
}
    def get_media_requests(self,item,info):
        for image_url in item['image_url']:
            self.default_headers['referer'] = image_url
            yield Request(image_url,headers=self.default_headers)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        print 'download now'
        item['image_paths'] = image_paths
        return item
