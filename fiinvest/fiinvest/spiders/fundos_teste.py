import scrapy
from scrapy_playwright.page import PageMethod

"""
BTN_POPUP = '//*[@id="popup-close-button"]'
BTN_SELECT_COLS = '//*[@id="colunas-ranking__select-button"]'
BTN_SELECT_ALL_COLS = '/html/body/div[6]/div[1]/div/div[2]/div[2]/ul/li[1]/label/span'
COLUMN = '/html/body/div[6]/div[2]/div/div/div/table/thead/tr/th' #30
ROW = '/html/body/div[6]/div[2]/div/div/div/table/tbody/tr' #430
 """
class FundosSpider(scrapy.Spider):
    name = "teste"
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
