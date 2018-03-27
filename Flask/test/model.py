from flask import Flask
from flask_mongoengine import MongoEngine
import datetime

app = Flask(__name__)

#Config the BD with MongoDB

app.config["MONGODB_SETTINGS"] = {"db":"dexter-api"}

#Create an instance with DB

db = MongoEngine(app)

class Users(db.Document):
    nome = db.StringField()
    email = db.StringField(unique=True)
    data_cadastro = db.DateTimeField(defaults=datetime.datetime.now())

class Groups(db.Document):
    nome = db.StringField(unique=True)
    integrantes = db.ListField()

# Create content on DB

if __name__ == "__main__":
    u = Users()
    u.nome = "Teste"
    u.email = "teste-neves93@hotmail.com"
    u.save()
    print ("Usuario cadastrado com sucesso!!")
    g = Groups()
    g.nome = "Comercial"
    g.integrantes.append(u)
    g.save()
    print("Grupo cadastrado")
