from app import db


class Cafeteria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensa_id = db.Column(db.Integer, unique=False, nullable=False)
    mensa_name = db.Column(db.String(50), unique=False, nullable=False)
    date = db.Column(db.String(50), unique=False, nullable=False)
    meal = db.Column(db.String(200), unique=False, nullable=False)
    # some items are free --> save "free"
    price = db.Column(db.String(10), unique=False, nullable=False)
    category = db.Column(db.String(50), unique= False, nullable=False)