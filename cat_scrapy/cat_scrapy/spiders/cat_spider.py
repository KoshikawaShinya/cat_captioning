import scrapy


class CatSpiderSpider(scrapy.Spider):
    name = 'cat_spider'
    start_urls = ['https://photohito.com/dictionary/%E7%8C%AB/']

    def parse(self, response):
        for product in response.css('div.imgholder'):
            yield {
                    'title': product.css('img').attrib['title'],
                    'url' : product.css('img').attrib['data-original']
            }


        next_page = response.css('a[rel="next"]').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        
