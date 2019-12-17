import scrapy
from scrapy.http import FormRequest
from mensa.items import Mensa
import os
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
        all = Mensa()
        category_divs = response.xpath('//div[contains(@class, "container-fluid") and contains(@class, "splGroupWrapper")]')
        date_div = response.xpath('//div[@class="container-fluid"]')
        all["date"] = date_div.xpath('./div[contains(@class, "row") and contains(@class, "row-top-percent-1")]/div[@class="col-xs-12"]/span/text()').getall()
        mensa_id = str(self.resource_id)
        mensa_id_list = []
        mensa_id_list.append(mensa_id)
        all["mensa_id"] = mensa_id_list
        mensa_name = TUMarchstrasse.name
        mensa_name_list = []
        mensa_name_list.append(mensa_name)
        all["mensa_name"] = mensa_name_list

        for i in range(len(category_divs)):
            category = category_divs[i].xpath('.//div[@class="row"]/div/text()').get()
            field = category.lower()
            field_price = field + '_price'
            all[field] = category_divs[i].xpath('.//span/text()').getall()
            all[field_price] = category_divs[i].xpath('.//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
            
        yield all

            
            
