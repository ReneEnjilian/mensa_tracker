from flask import Blueprint
routes = Blueprint("routes", __name__)
from mensa.starter import start_scrapers
from app import app


@app.route("/")
def hello():
    return "this is a test"

@app.route("/test", methods=['GET'])
def scrap():
    start_scrapers()
    return "success"