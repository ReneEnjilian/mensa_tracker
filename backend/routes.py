from flask import Blueprint
routes = Blueprint("routes", __name__)
from mensa.starter import start_scrapers
from app import app


@app.route("/")
def hello():
    return "this is a test"

@app.route("/cafeterias", methods=['GET'])
def refresh_all_cafeterias():
    start_scrapers()
    return "success"

@app.route("/cafeterias/<int:id>", methods=['GET'])
def load_cafeteria(id):
    pass

@app.route("/cafeterias/<int:id>/<day>", methods=['GET'])
def load_cafeteria_for_day(id, day):
    pass