# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Mensa(scrapy.Item):
    mensa_name = scrapy.Field()
    mensa_id = scrapy.Field()
    date = scrapy.Field()
    vorspeisen = scrapy.Field()
    vorspeisen_price = scrapy.Field()
    salate = scrapy.Field()
    salate_price = scrapy.Field()
    suppen = scrapy.Field()
    suppen_price = scrapy.Field()
    aktionen = scrapy.Field()
    aktionen_price = scrapy.Field()
    essen = scrapy.Field()
    essen_price = scrapy.Field()
    beilagen = scrapy.Field()
    beilagen_price = scrapy.Field()
    desserts = scrapy.Field()
    desserts_price = scrapy.Field()

class Personal(scrapy.Item):
    mensa_name = scrapy.Field()
    mensa_id = scrapy.Field()
    date = scrapy.Field()
    first = scrapy.Field()
    first_price = scrapy.Field()
    second = scrapy.Field()
    second_price = scrapy.Field()
    third = scrapy.Field()
    third_price = scrapy.Field()
    fourth = scrapy.Field()
    fourth_price = scrapy.Field()
    fifth = scrapy.Field()
    fifth_price = scrapy.Field()
    sixth = scrapy.Field()
    sixth_price = scrapy.Field()
    seventh = scrapy.Field()
    
