#coding=utf-8
import sys
import scrapy
import codecs
import time
import json
import os

from tutorial.xianyu_macpro_item import Item

def convert_to_builtin_type(obj): repr(obj)

if sys.getdefaultencoding() != 'gbk':  
    reload(sys)  
    sys.setdefaultencoding('gbk')  
default_encoding = sys.getdefaultencoding()  

ISOTIMEFORMAT='%Y-%m-%d'
ISOTIMEFORMAT_2='%H-%M'
current_time = time.strftime( ISOTIMEFORMAT, time.localtime() )
current_time_second = time.strftime( ISOTIMEFORMAT_2, time.localtime() )
print current_time

class xianyuSpider(scrapy.spiders.Spider):
    name = "xianyu"
    allowed_domains = ["taobao.com"]
    start_urls = [
	"https://s.2.taobao.com/list/list.htm?q=macbook+pro&search_type=item&app=shopsearch"
    ]
    i = 2
    while i < 101:
    	start_urls.append("https://s.2.taobao.com/list/list.htm?spm=2007.1000337.0.0.imx2BY&st_trust=1&page=%s&q=macbook+pro&ist=0" %i)
	i = i + 1

    def parse(self, response):
#	print response.xpath('//div[@id="J_ItemListsContainer"]/ul/li/div[@class="item-info"]/h4/a/text()').extract()
	items = []
	for sel in response.xpath('//div[@id="J_ItemListsContainer"]/ul/li'):
		item = Item()

    		title_list = sel.xpath('div[@class="item-info"]/h4/a/text()').extract()
		title = title_list[0]
		item["title"] = title_list[0]

		item_url_list = sel.xpath('div[@class="item-info"]/h4/a/@href').extract()
		item_url = item_url_list[0]
		item["item_url"] = item_url_list[0]

		item_id = item_url[item_url.index("id=")+3:]
		item["item_id"] = item_id

		price_list = sel.xpath('div[@class="item-info"]/div[@class="item-price price-block"]//em/text()').extract()
		price = price_list[0]
		item["price"] = price_list[0]

		description_list = sel.xpath('div[@class="item-info"]/div[@class="item-description"]/text()').extract()
		description = description_list[0]
		item["description"] = description_list[0]

#		list_time_list = sel.xpath('div[@class="item-info"]/div[@class="item-pub-info"]/span[@class="item-pub-time"]/text()').extract()
#		list_time = list_time_list[0]

		seller_location_list = sel.xpath('div[@class="seller-info-wrapper"]//div[@class="seller-location"]/text()').extract()
		seller_location = seller_location_list[0]
		item["seller_location"] = seller_location_list[0]
		
		items.append(item)

#		print json_result
	if not os.path.exists("../output/xianyu/"+current_time):
		os.mkdir("../output/xianyu/"+current_time)
        filename = "../output/xianyu/"+current_time+'/result'
	with codecs.open(filename, 'a', encoding='utf-8') as f:
		for item in items:
#			print item["item_id"]
            		f.write(item["title"]+'\t'+item["item_url"]+'\t'+item["item_id"]+'\t'+item["price"]+'\t'+item["description"]+'\t'+item["seller_location"]+'\n')
