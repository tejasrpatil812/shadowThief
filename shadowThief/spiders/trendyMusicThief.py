import scrapy
from ..items import ShadowThiefItem


class TrendyMusicThief(scrapy.Spider):
    name = 'trendyMusic'
    start_urls = [
        'https://www.billboard.com/charts/hot-100'
    ]

    def parse(self, response):
        muzik = ShadowThiefItem()
        trending_muziks = response.css('.chart-element__information')
        for i, trendy_muzik in enumerate(trending_muziks):
            muzik['position'] = i+1
            muzik['title'] = trendy_muzik.css('.chart-element__information__song::text').extract()
            muzik['author'] = trendy_muzik.css('.chart-element__information__artist::text').extract()
            muzik['source'] = 'BILLBOARD'
            yield muzik

