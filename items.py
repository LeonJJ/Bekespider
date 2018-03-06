# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BokespiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()#存储文章名
    url = scrapy.Field()#存储文章url
    hits = scrapy.Field()#存储文章点击数
    comment = scrapy.Field()#存储文章评论数

