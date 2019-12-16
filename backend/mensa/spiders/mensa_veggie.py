import scrapy
from scrapy.http import FormRequest
from mensa.items import Mensa

class VeggieMensa(scrapy.Spider):
    name = "VeggieMensa"
    start_urls = ["https://www.stw.berlin/xhr/speiseplan-wochentag.html"]

    def start_requests(self):
        yield FormRequest(url = self.start_urls[0], formdata={'resources_id': '631', "date": "2019-10-14"}, callback=self.parse)
    


    def parse(self, response):
        meals = response.xpath('//div[contains(@class, "container-fluid") and contains(@class, "splGroupWrapper")]')
        date_div = response.xpath('//div[@class="container-fluid"]')
        
        veggie = Mensa()

        veggie["date"] = date_div.xpath('.//span/text()').get()
        veggie["salats"] = meals[0].xpath('.//span/text()').getall()
        veggie["salatpreise"] = meals[0].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        veggie["suppen"] = meals[1].xpath('.//span/text()').getall()
        veggie["suppenpreise"] = meals[1].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()  
        veggie["aktionen"] = meals[2].xpath('.//span/text()').getall()       
        veggie["aktionspreise"] = meals[2].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        veggie["essen"] = meals[3].xpath('.//span/text()').getall()
        veggie["essenspreise"] = meals[3].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        veggie["beilagen"] = meals[4].xpath('.//span/text()').getall()
        veggie["beilagenpreise"] = meals[4].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        veggie["desserts"] = meals[5].xpath('.//span/text()').getall()
        veggie["dessertpreise"] = meals[5].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()


        yield veggie