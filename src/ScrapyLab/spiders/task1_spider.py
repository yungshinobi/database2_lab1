import scrapy


class Task2Spider(scrapy.spiders.CrawlSpider):
    name="task1"
    start_urls = [
        "https://stejka.com/rus/vinnickaja/"
    ]

    def parse(self, response):
        for text in response.xpath("//ul[@class='ulclear bywidth']"):
            yield {
                'url': response.url,
                'text': text.select("//div[@class='text']/a/text()").extract(),
                'images': text.select("//div[@class='foto']/@style").extract(),
                #'images': text.xpath('substring-before(substring-after(//div[@class=\'foto\']/@style, "background-image: url(\'"), "\')")').extract(),
            }

        for a in response.xpath("//div[@class='obl']").xpath(".//a"):
            yield response.follow(a, callback=self.parse)
