# -*- coding: utf-8 -*-
import scrapy

class GoodreadsSpider(scrapy.Spider):
    name = 'Goodreads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/quotes']

    def parse(self, response):
        with open('quotes.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        data = {}
        data['quotes'] = response.xpath('//div[@class="quoteText"]/text()').extract()
        
        yield data

        next_page = response.xpath('//a[@class="next_page"]/@href').extract_first()
        if next_page:
            url = 'https://www.goodreads.com' + next_page
            yield scrapy.Request(url, self.parse)
