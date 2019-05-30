# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import JobItem


class JobsSpiderSpider(scrapy.Spider):
    name = 'jobs_spider'
    start_urls = ['https://news.ycombinator.com/jobs']

    def parse(self, response):
        jobsTable = response.xpath('//table[@class="itemlist"]')

        xPath = './/tr[@class="athing"]//td[@class="title"]/a'
        location = jobsTable.xpath(xPath + '/@href').extract()
        company_info = jobsTable.xpath(xPath + '/text()').extract()

        xPath = './/tr//td[@class="subtext"]//span/a'
        age = jobsTable.xpath(xPath + '/text()').extract()
        for index in range(len(location)):
            item = JobItem()
            item["location"] = location[index]
            item["company_name"] = company_info[index]
            item["position"] = company_info[index]
            item["age"] = age[index]
            print('*****************************')
            print(item)
            yield item
