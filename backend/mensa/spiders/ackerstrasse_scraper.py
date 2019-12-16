import scrapy
from scrapy.http import FormRequest
from mensa.items import Mensa

class TUAckerstrasse(scrapy.Spider):
    name = "Ackerstrasse"
    start_urls = ["https://www.stw.berlin/xhr/speiseplan-wochentag.html"]

    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url=url, formdata={'resources_id': '539', "date": "2019-10-21"}, callback=self.parse)
    

    def parse(self, response):
        
        ackerstr = Mensa()
        meals = response.xpath('//div[contains(@class, "container-fluid") and contains(@class, "splGroupWrapper")]')
        date_div = response.xpath('//div[@class="container-fluid"]')

        ackerstr["date"] = date_div.xpath('.//span/text()').get()
        ackerstr["salats"] = meals[0].xpath('.//span/text()').getall()
        ackerstr["salatpreise"] = meals[0].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        ackerstr["essen"] = meals[1].xpath('.//span/text()').getall()
        ackerstr["essenspreise"] = meals[1].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        ackerstr["beilagen"] = meals[2].xpath('.//span/text()').getall()
        ackerstr["beilagenpreise"] = meals[2].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()

        yield ackerstr