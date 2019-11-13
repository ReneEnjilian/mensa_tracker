import scrapy
from scrapy.http import FormRequest
from mensa.items import Mensa
# test
#from mathe_cafe_spider import Mathecafe

class TUMarchstrasse(scrapy.Spider):
    name = "AllTU"
    start_urls = ["https://www.stw.berlin/xhr/speiseplan-wochentag.html"]
    resource_id = ""
    date = ""
    
    def __init__(self, id, date):
        self.resource_id = id
        self.date = date

    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url=url, formdata={'resources_id': self.resource_id, "date": self.date}, callback=self.parse)

    def parse(self, response):
        marchstr = Mensa()
        category_divs = response.xpath('//div[contains(@class, "container-fluid") and contains(@class, "splGroupWrapper")]')
        date_div = response.xpath('//div[@class="container-fluid"]')
        marchstr["date"] = date_div.xpath('./div[contains(@class, "row") and contains(@class, "row-top-percent-1")]/div[@class="col-xs-12"]/span/text()').getall()

        for i in range(len(category_divs)):
            category = category_divs[i].xpath('.//div[@class="row"]/div/text()').get()
            field = category.lower()
            field_price = field + '_preis'
            marchstr[field] = category_divs[i].xpath('.//span/text()').getall()
            marchstr[field_price] = category_divs[i].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        yield marchstr
        
            
            
