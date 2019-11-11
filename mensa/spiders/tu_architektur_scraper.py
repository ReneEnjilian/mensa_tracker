import scrapy
from scrapy.http import FormRequest
from mensa.items import Mensa

class TUArchitektur(scrapy.Spider):
    name = "Architektur"
    start_urls = ["https://www.stw.berlin/xhr/speiseplan-wochentag.html"]

    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url=url, formdata={'resources_id': '540', "date": "2019-10-21"}, callback=self.parse)

    def parse(self, response):
        architektur = Mensa()
        meals = response.xpath('//div[contains(@class, "container-fluid") and contains(@class, "splGroupWrapper")]')
        date_div = response.xpath('//div[@class="container-fluid"]')
        
    

        architektur["date"] = date_div.xpath('.//span/text()').get()
        architektur["salats"] = meals[0].xpath('.//span/text()').getall()
        architektur["salatpreise"] = meals[0].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        architektur["suppen"] = meals[1].xpath('.//span/text()').getall()
        architektur["suppenpreise"] = meals[1].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()  
        architektur["essen"] = meals[2].xpath('.//span/text()').getall()
        architektur["essenspreise"] = meals[2].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        architektur["beilagen"] = meals[3].xpath('.//span/text()').getall()
        architektur["beilagenpreise"] = meals[3].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()

        yield architektur
