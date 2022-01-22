# Import library
import scrapy
from ..items import AmazonItem

# Create Spider class
class AmazonSpider(scrapy.Spider):
    # Name of spider
    name = 'amazon'
    allowed_domains = ['amazon.com']
    # Website you want to scrape
    start_urls = [
        'https://www.amazon.co.uk/s?k=moisturizer&crid=1OO2ZUVX8ZJ9R&sprefix=moisturizer%2Caps%2C70&ref=nb_sb_noss_2'
    ]
    # Parses the website
    def parse(self, response):
        items = AmazonItem()
        prod_name = response.css('.a-color-base.a-text-normal::text').extract()
        prod_price = response.css('.a-price-whole::text').extract()

        items['name'] = prod_name
        items['price']= prod_price

        yield items
