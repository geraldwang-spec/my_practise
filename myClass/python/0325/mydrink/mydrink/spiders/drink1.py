# import scrapy
#
#
# class Drink1Spider(scrapy.Spider):
#     name = "drink1"
#     allowed_domains = ["www.drinks.com.tw"]
#     start_urls = ["https://www.drinks.com.tw/productlist.aspx?Id=7"]
#
#     def parse(self, response):
#         container=response.xpath("//div[@id='productlist']")
#         for item in container.xpath(".//a[contains(@class, 'product-list-title')]"):
#             name = item.xpath("text()").get()   
#             yield {
#                     "name" : name,
#                     }
#
#
import scrapy

class Drink1Spider(scrapy.Spider):
    name = "drink1"

    def start_requests(self):
        urls = ["https://www.drinks.com.tw/productlist.aspx?Id=7"]
        for url in urls:
            yield scrapy.Request(url, headers={
                "User-Agent": "Mozilla/5.0"
            })

    def parse(self, response):
        for item in response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' product-list ')]"):

            name = item.xpath(".//a[contains(concat(' ', normalize-space(@class), ' '), ' product-list-title ')]/text()").get()

            price = item.xpath(".//div[contains(concat(' ', normalize-space(@class), ' '), ' product-list-price ')]/text()").get()
            
            abv = item.xpath(".//div[contains(concat(' ', normalize-space(@class), ' '), ' product-list-sub ')]/text()").get()
            yield {
                "酒名": name.strip() if name else None,
                "價格": price.strip() if price else None,
                "濃度": abv.strip() if abv else None
            }


