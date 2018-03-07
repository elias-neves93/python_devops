from flask import Blueprint,jsonify,request
from model import Groups
import json

groups = Blueprint("groups",__name__)

@groups.route("/grupos/", methods=["GET"])
def list_groups():
    list_groups = json.loads(Groups.objects.to_json())
    return jsonify({"message":list_groups})

@groups.route("/grupos/",methods=["POST"])
def add_groups():
    try:
        data = request.get_json()
        g = Groups()
        for key in data.keys():
            setattr(g,key,data[key])
        g.save()
        return jsonify({"message":"Grupo cadastrado com sucesso!"})
    except Exception as e:
        return jsonify({"message":"Falhou ao cadastrar grupo: {}".format(e)})

@groups.route("/grupos/<id>",methods=["GET"])
def select_groups(id):
    g = json.loads(Groups.objects(id=id).to_json())
    data = {"grupo":g}
    return jsonify(data)

@groups.route("/grupos/<id>",methods=["PUT"])
def update_groups(id):
    try:
        data = request.get_json()
        g = Groups.objects(id=id).first()
        for key in data.keys():
            setattr(g,key,data[key])
        g.save()
        dados = {"message":"Atualizando o grupo ID: ".format(id)}
        return jsonify(dados)
    except Exception as e:
        return jsonify({"message":"Falhou ao atualizar: ".format(e)})

@groups.route("/grupos/<id>",methods=["DELETE"])
def delete_groups(id):
    g = Groups.objects(id=id)
    g.delete()
    data = {"message":"Deletar grupo id: {}".format(id)}
    return jsonify(data)
