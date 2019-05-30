# -*- coding: utf-8 -*-
import scrapy
from scrapy_spider.items import JobItem
from scrapy_spider.utils import get_company_name, get_position, get_location


class JobsSpiderSpider(scrapy.Spider):
    name = 'jobs_spider'
    start_urls = ['https://news.ycombinator.com/jobs']

    def parse(self, response):
        jobsTable = response.xpath('//table[@class="itemlist"]')

        xPath = './/tr[@class="athing"]//td[@class="title"]/a'
        details = jobsTable.xpath(xPath + '/@href').extract()
        company_info = jobsTable.xpath(xPath + '/text()').extract()

        xPath = './/tr//td[@class="subtext"]//span/a'
        age = jobsTable.xpath(xPath + '/text()').extract()
        for index in range(len(company_info)):
            item = JobItem()
            item["location"] = get_location(company_info[index])
            item["company_name"] = get_company_name(company_info[index])
            item["position"] = get_position(company_info[index])
            item["age"] = age[index]
            item["details"] = details[index]
            print('*****************************')
            yield item
