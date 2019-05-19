import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_url = [
    'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.css('title').extract()
        yield { 'titletext' : title }
