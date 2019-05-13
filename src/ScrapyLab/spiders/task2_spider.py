import scrapy
from scrapy.spiders import CrawlSpider


class Task2Spider(CrawlSpider):
    max_pages = 3
    name = "task2"
    start_urls = [
        "https://mebli-lviv.com.ua/ua/kitchen_kuhni/?page=1"
    ]
    next_page = "https://mebli-lviv.com.ua/ua/kitchen_kuhni/?page=2"

    def parse(self, response):
        for product in response.xpath('//div[@class="product-block item-default clearfix"]'):
            yield {
                'price': product.xpath('.//span[@class="special-price"]/text()').extract(),
                'title': product.xpath(".//h3[@class='name']/a/text()").extract(),
                'img':  product.xpath(".//img[@class='img-responsive']/@src").extract(),
            }

            # self.next_page = self.next_page[:-2] + str((int(self.next_page[76]) + 1)) + "/"
            #
            # next_page = self.next_page
            # if next_page is not None and int(next_page[76]) <= self.max_pages:
            #     next_page = response.urljoin(next_page)
            #     yield scrapy.Request(next_page, callback=self.parse)