import scrapy


class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for product in response.css('div.product-item-info'):
            yield {
                    'name': product.css('a.product-item-link::text').get(),
                    'price' : product.css('span.price::text').get().replace('£', ''),
                    'link' : product.css('a.product-item-link').attrib['href']
            }

        
        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)

