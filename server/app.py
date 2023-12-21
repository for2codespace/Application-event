import os

from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

from models import db
from resources import api
from sqlalchemy import text

load_dotenv()
app = Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('PRODUCTION_DATABASE_URL')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)
api.init_app(app)

with app.app_context():
    db.create_all()
    print(*db.session.execute(text("""
        SELECT table_name 
        FROM information_schema.tables;
    """)).fetchall(), sep="\n")


if __name__ == '__main__':
    app.run(host='0.0.0.0')