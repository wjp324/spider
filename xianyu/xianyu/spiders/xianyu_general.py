# -*- coding: utf-8 -*-
import scrapy
import re
from xianyu.macbookpro import MacBookPro 

class XianyuGeneralSpider(scrapy.Spider):
	name = "xianyu_general"
	allowed_domains = ["taobao.com"]
	start_urls = ['https://s.2.taobao.com/list/list.htm?q=macbook+pro&search_type=item&app=shopsearch']
	items = []

#	for i in range(2, 101):
#		start_urls.append('https://s.2.taobao.com/list/list.htm?q=MacBook&search_type=item&app=shopsearch&page=%s' % i)
	def parse_inner(self, response):
		item = MacBookPro()
		url = response.url
#		item_id = response.url[response.url.index("id=")+3:]
#		item["item_id"] = item_id
	
	def parse(self, response):
#		for sel in response.xpath('//div[@id="J_ItemListsContainer"]/ul/li'):
#			item = MacBookPro()
#			item_url_list = sel.xpath('div[@class="item-info"]/h4/a/@href').extract()
#			item_url = item_url_list[0]
#			yield scrapy.Request('https://'+item_url, callback=self.parse_inner)
		print response
'''
		selx = response.xpath('//div[@id="J_ItemListsContainer"]/ul/li')
		sel = selx[0]
		item = MacBookPro()
		item_url_list = sel.xpath('div[@class="item-info"]/h4/a/@href').extract()
		item_url = item_url_list[0]
		print item_url
		yield scrapy.Request('https://'+item_url, callback=self.parse_inner)
'''

