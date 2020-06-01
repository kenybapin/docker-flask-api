import os
import json
import random

from werkzeug.utils import secure_filename
from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for
)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config.from_object("api_sf2.config.Config")
db = SQLAlchemy(app)


# DataBase Init
class Char(db.Model):
    __tablename__ = "characters"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __init__(self, name):
        self.name = name

class Facts(db.Model):
    __tablename__ = "facts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    char_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    text = db.Column(db.String, nullable=False)
    char = db.relationship("Char", backref=db.backref("characters", uselist=False))

    def __init__(self, char_id, text):
        self.char_id = char_id
        self.text = text

# Routes : Endpoint http://localhost:5000

@app.route('/', methods=['GET'])
def index():
    return 'SF2 API - Random facts - Welcome', 200


@app.route('/<string:character>/facts', methods=['GET', 'POST'])
def char_results(character):

    if request.method == 'POST':
        mytext = request.form['mytext']
        
        myreq = db.session.execute("select public.characters.id FROM public.characters, public.facts WHERE public.facts.char_id=public.characters.id AND public.characters.name = :mystring", {"mystring": character}).first()
        myid=myreq[0]

        db.session.execute("INSERT INTO public.facts (char_id, text) VALUES (:i , :t)", {"i": myid, "t": mytext})
        db.session.commit()

    cols = ['id', 'name', 'text']
    char_data = db.session.execute("select public.characters.id, public.characters.name, public.facts.text FROM public.characters, public.facts WHERE public.facts.char_id=public.characters.id AND public.characters.name = :mystring", {"mystring": character}).fetchall()
    char_result = [{col: getattr(d, col) for col in cols} for d in char_data]  
    return jsonify(char_result=char_result), 200


@app.route('/all/facts', methods=['GET'])
def all_results():
    cols = ['id', 'name', 'text']
    data = Facts.query.join(Char).add_columns(Char.id, Char.name, Facts.text).filter(Char.id == Facts.char_id)
    result = [{col: getattr(d, col) for col in cols} for d in data]
    return jsonify(result=result), 200



@app.route('/random/facts', methods=['GET'])
def random_results():
    cols = ['id', 'name', 'text']
    random_query = db.session.execute("select name from public.characters OFFSET floor(random()*17) LIMIT 1").first()
    random = random_query[0]

    char_data = db.session.execute("select public.characters.id, public.characters.name, public.facts.text FROM public.characters, public.facts WHERE public.facts.char_id=public.characters.id AND public.characters.name = :random", {"random": random}).fetchall()
    char_result = [{col: getattr(d, col) for col in cols} for d in char_data]  
    return jsonify(char_result=char_result), 200


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404