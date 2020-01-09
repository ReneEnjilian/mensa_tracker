import scrapy
from mensa.items import Personal

class Mathecafe(scrapy.Spider):
    name = "Mathecafe"
    start_urls = ["http://singh-catering.de/cafe/"]

    def parse(self, response):
        top_layer = response.xpath('//article[@id="post-69"]/section[@class="article__content"]') 
        menu_lists = top_layer.xpath('.//div[contains(@class, "menu-list") and contains(@class, "menu-list__dotted")]') 

        mc = Personal()
        for i in range(len(menu_lists)):    # 3 iterationen
            
            meals = menu_lists[i].xpath('.//ul[@class="menu-list__items"]')
            days = menu_lists[i].xpath('.//h2[@class="menu-list__title"]')
           
            for j in range(len(days)):
                mensa_name = Mathecafe.name
                mc["mensa_id"] = ["1"]
                mensa_name_list = []
                mensa_name_list.append(mensa_name)
                mc["mensa_name"] = mensa_name_list
                #mc["mensa_id"] = []
                mc["date"] = days[j].xpath('./text()').getall()
                
                mc["first"] = meals[j].xpath('.//li[1]//h4/span[@class="item_title"]/text()').getall()
                mc["first_price"] = meals[j].xpath('.//li[1]//span[@class="menu-list__item-price"]/text()').getall()
                mc["second"] = meals[j].xpath('.//li[2]//h4/span[@class="item_title"]/text()').getall()
                mc["second_price"] = meals[j].xpath('.//li[2]//span[@class="menu-list__item-price"]/text()').getall()
                mc["third"] = meals[j].xpath('.//li[3]//h4/span[@class="item_title"]/text()').getall()
                mc["third_price"] = meals[j].xpath('.//li[3]//span[@class="menu-list__item-price"]/text()').getall()
                yield mc
            

                





