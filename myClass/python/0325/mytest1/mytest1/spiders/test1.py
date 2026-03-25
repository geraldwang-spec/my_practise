from webbrowser import get
import scrapy

# 如果有很多個a的話
# //a/text()
#
# 找屬性
# <a href='/news'>News</a>
# //a/@href
#
# 找類別
# <p class='logo'>用標籤找資料</p>
# //p[@class='logo']/text()
#
# 找 id
# <header id="site-header">
# //header[@id='site-header']
 

class Test1Spider(scrapy.Spider):
    name = "test1"
    allowed_domains = ["test1.com"]
    start_urls = ["file:///home/student/mydev/my_practise/myClass/python/0325/test1.html"]

    def parse(self, response):
        h1_text=response.xpath("//h1/text()").get()
        multi_a = response.xpath("//a/text()").getall()
        hrefs = response.xpath("//a/@href").getall()
        logo=response.xpath("//p[@class=\"logo\"]/text()").get()
        id=response.xpath("//header[@id='site-header']").get()
        yield{
                '抓到的h1':h1_text,
                '抓到a的內容':multi_a,
                'hrefs':hrefs,
                'logo_class':logo,
                'id':id,
                }


