from app import app, db
from routes import routes
from Models import Cafeteria



app.register_blueprint(routes)
db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
