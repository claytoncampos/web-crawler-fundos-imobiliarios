import scrapy
from scrapy_playwright.page import PageMethod

 
class FundosSpider(scrapy.Spider):
    name = "fundos"
    def start_requests(self):
        yield scrapy.Request("https://shoppable-campaign-demo.netlify.app/#/",
            callback=self.parse,
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("wait_for_selector", '.card-body'),
                ],
            },
        )

    async def parse(self, response):
        products = response.xpath('//*[@class="card-body"]')
        for product in products:
            yield {
            'title':product.xpath('.//*[@class="card-title"]/text()').get()
            }        
