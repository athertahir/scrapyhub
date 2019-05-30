# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    location = scrapy.Field()
    company_name = scrapy.Field()
    position = scrapy.Field()
    age = scrapy.Field()