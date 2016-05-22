# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MacBookPro(scrapy.Item):
	item_id = scrapy.Field()
	title = scrapy.Field()
	detail = scrapy.Field()
	model = scrapy.Field()
	size = scrapy.Field()
	cpu = scrapy.Field()
	modification = scrapy.Field()
	price = scrapy.Field()
	original_price = scrapy.Field()
	location = scrapy.Field()
	photo = scrapy.Field()
	last_upd = scrapy.Field()
	seller = scrapy.Field()
	comments = scrapy.Field()
