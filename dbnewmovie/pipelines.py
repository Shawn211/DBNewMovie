# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import codecs

class DbnewmoviePipeline(object):
    def process_item(self, item, spider):
        movie=[]

        moviename=[moviename for moviename in item['moviename'] if moviename!='']
        movierating=item['movierating']
        movieman=item['movieman']
        movieurl=item['movieurl']

        with codecs.open('movie','wb') as m:
        	#windows下，换行符采用'\r\n'
        	m.write('电影名字'+','+'电影评分'+','+'点评人数'+','+'电影链接'+'\r\n')
        	for x in range(len(moviename)):
        		m.write(str(moviename[x])+','+str(movierating[x])+','+str(movieman[x])+','+str(movieurl[x])+'\r\n')