# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShadowThiefItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    position = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    source = scrapy.Field()
    pass
