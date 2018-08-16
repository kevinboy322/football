# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.selector import Selector
from football.items import FootballItem

class ShoumiSpider(scrapy.Spider):
    name = 'shoumi'
    # allowed_domains = ['live.titan007.com']
    start_urls = ['http://live.titan007.com/']

    def parse(self, response):
        item = FootballItem()
        body = response.body
        selector = Selector(response)
        table = selector.xpath('//*[@id="button"]')
        print(table)
        item['body'] = table
        yield item
