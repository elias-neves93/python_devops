from flask import Blueprint,jsonify

groups = Blueprint("groups",__name__)

@groups.route("/grupos/")
def list_groups():
    data = {"message":"Aqui serão listados todos os groups"}
    return jsonify(data)

@groups.route("/grupos/",methods=["POST"])
def add_groups():
    data = {"message":"Aqui serão cadastrado novos groups"}
    return jsonify(data)

@groups.route("/grupos/<int:id>",methods=["GET"])
def select_groups(id):
    data = {"message":"Mostrat groupo de acordo com o id: {}".format(id)}
    return jsonify(data)

@groups.route("/grupos/<int:id>",methods=["PUT"])
def update_groups(id):
    data = {"message":"Atualizar grupo id: {}".format(id)}
    return jsonify(data)

@groups.route("/grupos/<int:id>",methods=["DELETE"])
def delete_groups(id):
    data = {"message":"Deletar grupo id: {}".format(id)}
    return jsonify(data)
