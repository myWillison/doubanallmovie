# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class movieItem(Item):
    # define the fields for your item here like:
    # name = Field()
    title, time, diretor, screen_writer, movie_type1, movie_type2, movie_length, score, people_num, rate1, rate2, rate3, rate4, rate5 = Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field(), Field()
class commentItem(Item):
    movie_name, username, score, time, comment, vote = Field(), Field(), Field(), Field(), Field(), Field()

