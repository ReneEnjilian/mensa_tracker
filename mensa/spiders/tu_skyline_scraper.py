import scrapy
from scrapy.http import FormRequest
from mensa.items import Mensa

class TUArchitektur(scrapy.Spider):
    name = "Skyline"
    start_urls = ["https://www.stw.berlin/xhr/speiseplan-wochentag.html"]

    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(url=url, formdata={'resources_id': '657', "date": "2019-10-21"}, callback=self.parse)

    def parse(self, response):
        skyline = Mensa()
        meals = response.xpath('//div[contains(@class, "container-fluid") and contains(@class, "splGroupWrapper")]')
        date_div = response.xpath('//div[@class="container-fluid"]')
        
    

        skyline["date"] = date_div.xpath('.//span/text()').get()
        skyline["salats"] = meals[0].xpath('.//span/text()').getall()
        skyline["salatpreise"] = meals[0].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        skyline["suppen"] = meals[1].xpath('.//span/text()').getall()
        skyline["suppenpreise"] = meals[1].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()  
        skyline["essen"] = meals[2].xpath('.//span/text()').getall()
        skyline["essenspreise"] = meals[2].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        skyline["beilagen"] = meals[3].xpath('.//span/text()').getall()
        skyline["beilagenpreise"] = meals[3].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        skyline["desserts"] = meals[4].xpath('.//span/text()').getall()
        skyline["dessertpreise"] = meals[4].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()

        yield skyline
