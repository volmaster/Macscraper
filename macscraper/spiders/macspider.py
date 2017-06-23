# -*- coding: utf-8 -*-
import scrapy
import json
from macscraper.items import MacscraperItem


class MacspiderSpider(scrapy.Spider):
    name = 'macspider'
    start_urls = ['https://map.mcdonalds.co.jp/api/poi?bounds=35.5000%2C138.942%2C35.8175%2C139.920']

    def parse(self, response):
        url = 'https://map.mcdonalds.co.jp/map/{}'
        json_response = json.loads(response.body)
        for shop in json_response:
            yield scrapy.Request(url.format(shop["key"]), callback=self.parse_shop)

    def parse_shop(self, response):
        item = MacscraperItem()
        item['name'] = response.xpath('//span[@class="shopName"]/text()').extract_first()
        item['capacity'] = response.xpath(
            '//div[@class="spec seat"]/span[@class="value"]/text()').extract_first()
        item['zipcode'] = response.xpath('//li[@class="postalCode"]/text()').extract_first()
        item['address'] = response.xpath('//li[@class="address"]/text()').extract_first()
        item['tel'] = response.xpath('//li[@class="phone"]/a/text()').extract_first()
        yield item
