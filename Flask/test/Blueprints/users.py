from flask import Blueprint,jsonify

users = Blueprint("users",__name__)

@users.route("/usuarios/")
def list_users():
    data = {"message":"Aqui serão listados todos os usuarios"}
    return jsonify(data)

@users.route("/usuarios/",methods=["POST"])
def add_users():
    data = {"message":"Aqui serão cadastrado novos usuarios"}
    return jsonify(data)

@users.route("/usuarios/<int:id>",methods=["GET"])
def select_users(id):
    data = {"message":"Mostrat usuario de acordo com o id: {}".format(id)}
    return jsonify(data)

@users.route("/usuarios/<int:id>",methods=["PUT"])
def update_users(id):
    data = {"message":"Atualizar usuario id: {}".format(id)}
    return jsonify(data)

@users.route("/usuarios/<int:id>",methods=["DELETE"])
def delete_users(id):
    data = {"message":"Deletar usuario id: {}".format(id)}
    return jsonify(data)
