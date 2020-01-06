# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Location(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    street_address = scrapy.Field()
    extended_address = scrapy.Field()
    locality = scrapy.Field()
    phone_number = scrapy.Field()
    opening_hours = scrapy.Field()
    overall_rating = scrapy.Field()
    rating_count = scrapy.Field()
    rating_details = scrapy.Field()
    
class RatingDetail(scrapy.Item):
    label = scrapy.Field()
    rating = scrapy.Field()
