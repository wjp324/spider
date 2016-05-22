import scrapy

class Item(scrapy.Item):
	title = scrapy.Field()
	item_url = scrapy.Field()
	item_id = scrapy.Field()
	price = scrapy.Field()
	description = scrapy.Field()	
	seller_location = scrapy.Field()
