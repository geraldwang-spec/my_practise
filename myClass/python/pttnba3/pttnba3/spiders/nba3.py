import scrapy


class Nba3Spider(scrapy.Spider):
    name = "nba3"
    allowed_domains = ["nba3.com"]
    start_urls = ["https://www.ptt.cc/bbs/nba/index.html"]

    def parse(self, response):
        for post in response.css('div.r-ent'):
            yield {
                    'title':post.css('div.title a::text').get() 
                    }
