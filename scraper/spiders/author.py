import scrapy


class AuthorSpider(scrapy.Spider):
    name = 'author'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://http://quotes.toscrape.com//']

    def parse(self, response):
        pass
