import scrapy


class Mlb2Spider(scrapy.Spider):
    name = "mlb2"
    allowed_domains = ["mlb2.com"]
    start_urls = ["https://www.ptt.cc/bbs/MLB/index.html"]

    def parse(self, response):
        for post in response.css('div.r-ent'):
            yield {
                    'title':post.css('div.title a::text').get() 

                    }
