from Models import Cafeteria
from app import db


class DBPipeline(object):
    def process_item(self, item, spider):
        
        # mensa_name = item["mensa_name"][0]
        # test = Cafeteria(mensa_name=mensa_name, mensa_id=1, date="test", meal="test", price="hallo", category="test")
        
        # db.session.add(test)
        # db.session.commit()

        # print("inserted", flush=True)

        self.insert_mathe_cafe(item, spider)

        return item
    
    def extract_fields(self, item):
        wanted_fields = []
        fields = item.keys()
        for field in fields:
            if "preis" not in field and  "price" not in field and "mensa" not in field and "date" not in field:
                wanted_fields.append(field)
        return wanted_fields


    def get_mensa_name_id(self, item, spider):
        if spider.name == "Mathecafe":
            item["mensa_name"][0] = spider.name
            item["mensa_id"][0] = 1
        elif spider.name == "Personalkantine":
            item["mensa_name"][0] = spider.name
            item["mensa_id"][0] = 2
        else:
            mensa_id = item["mensa_id"][0]
            if mensa_id == "321":
                item["mensa_name"][0] = "Hardenbergstrasse"
                item["mensa_id"][0] = 3
            elif mensa_id == "631":
                item["mensa_name"][0] = "Veggie"
                item["mensa_id"][0] = 4
            elif mensa_id == "540":
                item["mensa_name"][0] = "Architektur"
                item["mensa_id"][0] = 5
            elif mensa_id == "657":
                item["mensa_name"][0] = "Skyline"
                item["mensa_id"][0] = 6
            elif mensa_id == "538":
                item["mensa_name"][0] = "Marchstrasse"
                item["mensa_id"][0] = 7
            elif mensa_id == "539":
                item["mensa_name"][0] = "Ackerstrasse"
                item["mensa_id"][0] = 8

        return item

            
    def insert_to_db(self, mensa_id, mensa_name, date, meal, price, category):
        # print("####################", flush=True)
        # print(mensa_id, flush=True)
        # print(mensa_name, flush=True)
        # print(date, flush=True)
        # print(meal, flush=True)
        # print(price, flush=True)
        # print(category, flush=True)
        # print("####################", flush=True)

        row = Cafeteria(mensa_id=mensa_id, mensa_name=mensa_name, date=date, meal=meal, price=price, category=category)
        db.session.add(row)
        db.session.commit()
        # test = Cafeteria(mensa_name=mensa_name, mensa_id=1, date="test", meal="test", price="hallo", category="test")
        
        # db.session.add(test)
        # db.session.commit()



    def insert_mathe_cafe(self, item, spider):
        updated_item = self.get_mensa_name_id(item, spider)
        wanted_fields = self.extract_fields(item)
        date = updated_item["date"][0]
        mensa_name = updated_item["mensa_name"][0]
        mensa_id = updated_item["mensa_id"][0]
        for field in wanted_fields:
            category = updated_item[field]
            for i in range(len(category)):
                price_field = field + "_price"
                meal = category[i]
                price = updated_item[price_field][i]
                self.insert_to_db(mensa_id, mensa_name, date, meal, price, field)
                # print(field, flush=True)
                # print(meal, flush=True)
                # print(price, flush=True)






        

            

        