import time
import os
from dotenv import load_dotenv

from flask import Flask, render_template, send_file, redirect
from flask_cors import CORS

from models import db
from resources import api
from sqlalchemy import text


# load_dotenv() # for deployment without docker

app = Flask(__name__, static_folder='build/static', template_folder='build')
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)
api.init_app(app)

with app.app_context():
    tries = 0
    while tries < 10:
        try:
            db.create_all()
            break
        except db.ConnectionError as e:
            tries += 1
            print(f"[{tries:0>2}/10] Failed to connect to the database. Retrying...")
            time.sleep(3)


@app.route('/')
def index():
    return redirect('/groupes')


@app.route('/<string:path>')
def catch_all(path):
    static_files = [
        'index.html',
        'accet-manifest.json',
        'favicon.ico',
        'manifest.json',
        'logo192.png',
        'logo512.png',
        'logo.png',
        'image.jpg',
        'logo.svg',
        'robots.txt'
    ]
    if path in static_files:
        return send_file(f'build/{path}')
    else:
        return render_template('index.html')
