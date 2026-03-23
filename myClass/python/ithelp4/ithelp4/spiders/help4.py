from ast import parse
from curses import meta
from gc import callbacks
from typing import override
import scrapy
from scrapy.http import headers


class Help4Spider(scrapy.Spider):
    name = "help4"
    allowed_domains = ["ithelp.ithome.com.tw"]
      
    @override
    def start_requests(self) :
        start_urls = "https://ithelp.ithome.com.tw/"
        headers = {'User-Agent':'Mozilla/5.0'}
        yield scrapy.Request(url=start_urls, headers=headers,  callback=self.parse)

    def parse(self, response):
        for h3 in response.css('h3.qa-list__title'):
            headers = {'User-Agent':'Mozilla/5.0'}
            a = h3.css('a.qa-list__title-link')
            title =a.css('::text').get()
            link = a.css('::attr(href)').get()
            yield response.follow(link, headers=headers, callback=self.parse_detail, meta={'title':title})
            # yield {
            #         'title':a.css('::text').get().strip() 
            #         }
            #
    def parse_detail(self, response):
        content=response.css('div.markdown__style p::text').getall()
        yield {
                'title':response.meta['title'],
                'content':''.join(content)
                }

