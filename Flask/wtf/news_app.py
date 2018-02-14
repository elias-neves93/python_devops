from flask import flask
from wtf.views import cadastro, index, noticia, media

app = Flask("wtf")
app.config.from_object('wtf.settings')
