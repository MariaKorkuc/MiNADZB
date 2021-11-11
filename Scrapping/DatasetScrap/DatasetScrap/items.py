# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class DatasetscrapItem(scrapy.Item):
    # date = Field()
    # price = Field()
    # bedrooms = Field()
    # bathrooms = Field()
    # sqft_living = Field()
    # sqft_lot = Field()
    # floors = Field()
    # condition = Field()
    # sqft_above = Field()
    # sqft_base = Field()
    # yr_built = Field()
    # yr_renovation = Field()
    date = Field()
    state = Field()
    cases = Field()
    deaths = Field()
    confirmed_cases = Field()
    confirmed_deaths = Field()


