from Models import Cafeteria
from app import db


class DBPipeline(object):
    def process_item(self, item, spider):
        
        # mensa_name = item["mensa_name"][0]
        # test = Cafeteria(mensa_name=mensa_name, mensa_id=1, date="test", meal="test", price="hallo", category="test")
        
        # db.session.add(test)
        # db.session.commit()

        # print("inserted", flush=True)

        self.insert_mathe_cafe(item)

        return item
    
    def extract_fields(self, item):
        wanted_fields = []
        fields = item.keys()
        for field in fields:
            if "preis" not in field and  "price" not in field and "mensa" not in field and "date" not in field:
                wanted_fields.append(field)
       
        return wanted_fields

    def get_mensa_name(self, item):
        pass

    def insert_mathe_cafe(self, item):
        #mensa_name = item["mensa_name"][0]
        date = item["date"][0]
        mensa_id = 1
        wanted_fields = self.extract_fields(item)
        print("*********", flush=True)
        print(wanted_fields, flush=True)
        print("*********", flush=True)

        

            

        