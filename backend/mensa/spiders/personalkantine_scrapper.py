import scrapy
from mensa.items import Personal

class Personalkantine(scrapy.Spider):
    name = "Personalkantine"
    start_urls = ["http://personalkantine.personalabteilung.tu-berlin.de/"]

    def parse(self, response):

        # data of the full week (Mo-Fr)
        meal_plan = response.xpath('//section[@id="speisekarte"]//ul[@class="Menu__accordion"]/li')
        personal = Personal()

        for i in range(len(meal_plan)):
            mensa_name = Personalkantine.name
            mensa_name_list = []
            mensa_name_list.append(mensa_name)
            personal["mensa_name"] = mensa_name_list
            personal["mensa_id"] = ["1"]
            personal["date"] = meal_plan[i].xpath('.//h2/text()').getall()
            meals_of_the_day = meal_plan[i].xpath('.//ul/li')
            personal["first"] = meals_of_the_day[0].xpath('.//h4/text()').getall()
            personal["first_price"] = meals_of_the_day[0].xpath('.//span/text()').getall()
            personal["second"] = meals_of_the_day[1].xpath('.//h4/text()').getall()
            personal["second_price"] = meals_of_the_day[1].xpath('.//span/text()').getall()
            personal["third"] = meals_of_the_day[2].xpath('.//h4/text()').getall()
            personal["third_price"] = meals_of_the_day[2].xpath('.//span/text()').getall()
            personal["fourth"] = meals_of_the_day[3].xpath('.//h4/text()').getall()
            personal["fourth_price"] = meals_of_the_day[3].xpath('.//span/text()').getall()
            personal["fifth"] = meals_of_the_day[4].xpath('.//h4/text()').getall()
            personal["fifth_price"] = meals_of_the_day[4].xpath('.//span/text()').getall()
            personal["sixth"] = meals_of_the_day[5].xpath('.//h4/text()').getall()
            personal["sixth_price"] = meals_of_the_day[5].xpath('.//span/text()').getall()

            # Mittwoch clean preis
            yield personal
            
