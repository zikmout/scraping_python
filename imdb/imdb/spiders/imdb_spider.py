# -*- coding: utf-8 -*-
import scrapy

class BookItem(Item):
    images = Field()
    images_urls = Field()

    def parse_book(self, response):
        book = BookItem()
        relative_img_urls = response.css("div.iten.active > img::attr(src)").extract()
        book['image_urls'] = self.url_join(relative_img_urls, response)
        return book

    def url_join(self, urls, response):
        joined_urls  = []
        for url in urls:
            joined_urls.append(response.urljoin(url))

        return joined_urls

class ImdbSpiderSpider(scrapy.Spider):
    name = 'imdb_spider'
    allowed_domains = ['http://www.imdb.com/name/nm0000093/']
    start_urls = ['http://http://www.imdb.com/name/nm0000093//']

    def parse(self, response):
        pass

