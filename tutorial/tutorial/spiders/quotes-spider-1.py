import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes1"
    start_urls =['http://quotes.toscrape.com']
    def parse(self, response):
        self.logger.info('hello this is my first spider')
        pass