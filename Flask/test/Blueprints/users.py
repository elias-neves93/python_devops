from flask import Blueprint,jsonify,request
from model import Users
import json

users = Blueprint("users",__name__)

@users.route("/usuarios/", methods=["GET"])
def list_users():
    list_users = json.loads(Users.objects.to_json())
    return jsonify({"usuarios":list_users})

@users.route("/usuarios/",methods=["POST"])
def add_users():
    try:
        data = request.get_json()
        u = Users()
        for key in data.keys():
            setattr(u,key,data[key])
        u.save()
        return jsonify({"message":"Usuario cadastrado com sucesso!"})
    except Exception as e:
        return jsonify({"message":"Falhou ao cadastrar: {}".format(e)})

@users.route("/usuarios/<id>",methods=["GET"])
def select_users(id):
    u = json.loads(Users.objects(id=id).to_json())
    data = {"usuario":u}
    return jsonify(data)

@users.route("/usuarios/<id>",methods=["PUT"])
def update_users(id):
    try:
        data = requests.get_json()
        u = Users.objects(id=id).first()
        for key in data.keys():
            setattr(u,key,data[key])
        u.save()
        dados = {"message":"Atualizando o usuario ID: ".format(id)}
        return jsonify(dados)
    except Exception as e:
        return jsonify({"message":"Falhou ao atualizar: ".format(e)})

@users.route("/usuarios/<id>",methods=["DELETE"])
def delete_users(id):
    u = Users.objects(id=id)
    u.delete()
    data = {"message":"Deletar usuario id: {}".format(id)}
    return jsonify(data)
