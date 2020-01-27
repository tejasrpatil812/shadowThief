import scrapy
from ..items import ShadowThiefItem


class QuotesThief(scrapy.Spider):
    name = 'quotesShadow'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        quote = ShadowThiefItem()
        all_quotes = response.css('.quote')
        for quotes in all_quotes:
            title = quotes.css('.text::text').extract()
            author = quotes.css('.author::text').extract()
            tags = quotes.css('.tag::text').extract()
            quote['title'] = title
            quote['author'] = author
            quote['tags'] = tags
            yield quote

