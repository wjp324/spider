#!/bin/python
#coding=utf-8
import MySQLdb
import sys
import time
import mac_parse

## load data from file
ISOTIMEFORMAT='%Y-%m-%d'
current_time = time.strftime( ISOTIMEFORMAT, time.localtime() )
print current_time

try:
#	f = open("../output/xianyu/%s/result"% current_time,"r") 
	f = open("../output/xianyu/2016-05-06/result","r") 
	items = []
	for line in f.readlines():
		element = line.split('\t')
		element.append(current_time)
		#parse original file
		# --> get:
		#	1. size
		#	2. model
		#	3. made_year
		#	4. concern_flag
		result = mac_parse.parse_ori(element)
		element.extend(result)
		items.append(element)
except IOError, e:
	print e
	sys.exit(1)

## insert in mysql
try:
	conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="crawl",charset="utf8")
	cur = conn.cursor()

	sqli="insert into macpro (title,item_url,item_id,price,description,seller_location,date,size,model,year,cpu) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	cur.executemany(sqli,items)

	cur.close()
	conn.commit()
except Exception, e:
	conn.rollback()
	print e
	sys.exit(1)
finally:
	conn.close()
