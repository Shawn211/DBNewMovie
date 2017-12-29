# -*- coding: utf-8 -*-
import scrapy
import re
from dbnewmovie.items import DbnewmovieItem						#将我们需要爬的数据名称引入进来

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["movie.douban.com/chart"]
    start_urls = ['http://movie.douban.com/chart/']

    def parse(self, response):

    	moviename=response.xpath('//div[@class="pl2"]/a/text()').extract()
    	movierating=response.xpath('//span[@class="rating_nums"]/text()').extract()
    	movieman=response.xpath('//span[@class="pl"]/text()').extract()
    	movieurl=response.xpath('//div[@class="pl2"]/a/@href').extract()

    	items=DbnewmovieItem()

    	items['moviename']=[re.sub('/','',re.sub(' ','',re.sub('\n','',n))) for n in moviename]
    	items['movierating']=movierating
    	items['movieman']=[mvman.split('(')[1].split('人')[0] for mvman in movieman]
    	items['movieurl']=movieurl

    	yield items