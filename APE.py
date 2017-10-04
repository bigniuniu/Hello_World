# -*- coding: utf-8 -*-
import scrapy
from APE_3_comments.items import Ape3CommentsItem


class ApeSpider(scrapy.Spider):
    name = 'APE'
    #allowed_domains = ['https://movie.douban.com/subject/26883064/comments?status=P']
    baseURL = 'https://movie.douban.com/subject/26883064/comments'
    start_urls = ['https://movie.douban.com/subject/26883064/comments?status=P']

    def parse(self, response):
        node_set = response.xpath('//p[@class = ""]')
        for node in node_set:
            items = Ape3CommentsItem()
            comment = node.xpath('./text()').extract()[0]
            items['comments'] = comment
            yield items

        next_link = response.xpath('//a[@class="next"]/@href').extract()[0]
        if len(next_link):
            url = self.baseURL + next_link
            yield scrapy.Request(url, callback = self.parse)

