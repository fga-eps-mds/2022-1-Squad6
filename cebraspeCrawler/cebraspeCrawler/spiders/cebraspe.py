import scrapy


class CebraspeSpider(scrapy.Spider):
    name = 'cebraspe'
    allowed_domains = ['www.cebraspe.org.br']
    start_urls = ['http://www.cebraspe.org.br/']

    def parse(self, response):
        pass
