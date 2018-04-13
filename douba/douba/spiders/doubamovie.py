# -*- coding: utf-8 -*-
import scrapy
from douba.items import DoubaItem

class DoubamovieSpider(scrapy.Spider):
    name = 'doubamovie'
    allowed_domains = ['movie.douban.com']
    url = "https://movie.douban.com/top250?start="
    offset = 0
    start_urls = (url + str(offset),)

    def parse(self, response):
        item = DoubaItem()
        for each in response.xpath('//div[@class="info"]'):
            item['title'] = each.xpath('.//div[@class="hd"]/a/span/text()').extract()[0]
            item['bd'] = each.xpath('.//div[@class="bd"]/p/text()').extract()[0]
            item['star'] = each.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            quote = each.xpath('.//div/p[@class="quote"]/span/text()').extract()
            if len(quote) != 0:
                item['quote'] =quote[0]


            yield item
        if self.offset < 225:
            self.offset += 25

        yield scrapy.Request(self.url + str(self.offset),callback = self.parse)