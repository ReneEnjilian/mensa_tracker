from Models import Cafeteria
from app import db


class DBPipeline(object):
    def process_item(self, item, spider):
        
        mensa_name = item["mensa_name"][0]
        test = Cafeteria(mensa_name=mensa_name, mensa_id=1, date="test", meal="test", price="test", category="test")
        
        db.session.add(test)
        db.session.commit()



        return item