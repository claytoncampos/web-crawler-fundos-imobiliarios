import scrapy


class FundosSpider(scrapy.Spider):
    name = "fundos"
    allowed_domains = ["www.fundsexplorer.com.br"]
    start_urls = ["https://www.fundsexplorer.com.br/ranking"]

    def parse(self, response):
        pass
