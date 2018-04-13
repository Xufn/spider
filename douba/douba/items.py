# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #影片名
    title = scrapy.Field()
    #简介
    bd = scrapy.Field()
    #评分
    star = scrapy.Field()
    #quote
    quote = scrapy.Field()
