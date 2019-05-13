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
        for product in response.xpath('//div[@class="products-block"]'):
            yield {
                #'title': product.css('div.product-meta-inner a::title').extract(),
                #'desc': product.css('div.product_item_text::text').extract_first(),
                #'price': product.css('div.products_list_price::text').extract(),
                #'img': response.urljoin(product.css('div.img-responsive img::attr(src)').extract_first()),
                'title': product.xpath("//div[@class='review clearfix']/h3[@class='name']/a/text()").extract(),
                'img':  product.xpath("//div[@class='images clearfix']/a[@class='img']/img[@class='img-responsive']/@src").extract(),
            }

        # self.next_page = self.next_page[:-2] + str((int(self.next_page[76]) + 1)) + "/"
        #
        # next_page = self.next_page
        # if next_page is not None and int(next_page[76]) <= self.max_pages:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)