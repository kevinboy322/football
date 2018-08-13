# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class ShoumiSpider(scrapy.Spider):
    name = 'shoumi'
    # allowed_domains = ['live.titan007.com']
    start_urls = ['http://live.titan007.com/']

    def parse(self, response):
        html = response.body
        all_a = BeautifulSoup(html, 'lxml').find('table', id='table_live').find_all('a')
        print(all_a)
        # all = BeautifulSoup(html)
        # items = []
        # num = 1
        # for sel in :
        #     if num == 1:
        #         num += 1
        #         continue
        #     elif sel.xpath('td[3][text()="完"]'):
        #         items["matchId"] = sel.
        pass
