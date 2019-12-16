import scrapy
from scrapy.http import FormRequest
from scrapy.selector import Selector
from mensa.items import Mensa

class TUMensa(scrapy.Spider):
    name = "TUMensa"
    start_urls = ["https://www.stw.berlin/xhr/speiseplan-wochentag.html"]

    def start_requests(self):
        for url in self.start_urls:
            #print(url)
            yield FormRequest(url=url, formdata={'resources_id': '321', "date": "2019-10-21"}, callback=self.parse)
    


    def parse(self, response):
        meals_divs = response.xpath('//div[contains(@class, "container-fluid") and contains(@class, "splGroupWrapper")]').getall()
        date_divs = response.xpath('//div[@class="container-fluid"]').get()
        date_divs_list = []
        date_divs_list.append(date_divs)
        all_divs = date_divs_list + meals_divs
        hauptmensa = Mensa()
          
        hauptmensa["date"] = Selector(text=all_divs[0]).xpath('//span/text()').get()
        hauptmensa["vorspeise"] = Selector(text=all_divs[1]).xpath('//span/text()').get()
        hauptmensa["vorspeisepreis"] = Selector(text=all_divs[1]).xpath('//div[contains(@class, "row") and contains(@class, "splMeal")]/div[contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').get()            
        hauptmensa["salats"] = Selector(text=all_divs[2]).xpath('//span/text()').getall()
        hauptmensa["salatpreise"] = Selector(text=all_divs[2]).xpath('//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        hauptmensa["suppen"] = Selector(text=all_divs[3]).xpath('//span/text()').getall()
        hauptmensa["suppenpreise"] = Selector(text=all_divs[3]).xpath('//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()  
        hauptmensa["aktionen"] = Selector(text=all_divs[4]).xpath('//span/text()').getall()       
        hauptmensa["aktionspreise"] = Selector(text=all_divs[4]).xpath('//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        hauptmensa["essen"] = Selector(text=all_divs[5]).xpath('//span/text()').getall()
        hauptmensa["essenspreise"] = Selector(text=all_divs[5]).xpath('//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        hauptmensa["beilagen"] = Selector(text=all_divs[6]).xpath('//span/text()').getall()
        hauptmensa["beilagenpreise"] = Selector(text=all_divs[6]).xpath('//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()
        hauptmensa["desserts"] = Selector(text=all_divs[7]).xpath('//span/text()').getall()
        hauptmensa["dessertpreise"] = Selector(text=all_divs[7]).xpath('//div[contains(@class, "col-xs-6") and contains(@class, "col-md-3") and contains(@class, "text-right")]/text()').getall()

         
        yield hauptmensa
      
        #col-xs-6 col-md-3 text-right
        #col-xs-6 col-md-3 text-right