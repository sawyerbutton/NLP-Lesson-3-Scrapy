import scrapy
class QuotesSpider(scrapy.Spider):
    name = "quotes2"
start_urls = ['http://quotes.toscrape.com']
def parse(self, response):
        self.logger.info('hello this is my first spider')
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            yield {
                'text': quote.css('.text::text').get(),
                'author': quote.css('.author::text').get(),
                'tags': quote.css('.tag::text').getall(),
            }