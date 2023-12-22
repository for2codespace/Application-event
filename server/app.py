import os
from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS
from waitress import serve

from models import db
from resources import api
from sqlalchemy import text


load_dotenv()
app = Flask(__name__, static_folder='static')
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('PRODUCTION_DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)
api.init_app(app)

with app.app_context():
    db.create_all()


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=403)
    # run `waitress-serve --port=403 app:app` in console or
    # run this file: `python app.py`