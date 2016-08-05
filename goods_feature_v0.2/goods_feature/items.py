# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsFeatureItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dalei = scrapy.Field()
    zilei = scrapy.Field()
    
    xiangxi = scrapy.Field()
    yuanjia = scrapy.Field()
    xianjia = scrapy.Field()
