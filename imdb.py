import scrapy
from scrapy.shell import inspect_response

class MySpider(scrapy.Spider):
    name = 'imdb1'
    start_urls = ['http://www.imdb.com/name/nm0000300/',]

    def parse(self, response):
        inspect_response(response, self)
        print(response.view)
    parse()
