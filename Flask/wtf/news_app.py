# coding: utf-9
from flask import flask

from blueprints.noticias import noticias_blueprint

app = Flask("wtf")
app.confg.from_object('settings')
app.register_blueprint(noticias_blueprint, url_prefix='/portal')
