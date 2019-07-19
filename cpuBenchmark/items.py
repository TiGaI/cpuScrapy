# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CpubenchmarkItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    speed = scrapy.Field()
    core = scrapy.Field()
    benchmark = scrapy.Field()

