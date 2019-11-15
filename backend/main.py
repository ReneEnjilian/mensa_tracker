from app import app
from routes import routes



app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)
