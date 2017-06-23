# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MacscraperItem(scrapy.Item):
    name = scrapy.Field()
    capacity = scrapy.Field()
    zipcode = scrapy.Field()
    address = scrapy.Field()
    tel = scrapy.Field()
