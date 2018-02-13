from flask import Flask
from flask import render_template
import json
from flask import make_response, abort
from flask import jsonify
from flask import request, current_app
import os
from werkzeug import secure_filename
from flask import request, redirect, url_for
from flask import Flask, session, redirect, url_for, escape, request

app = Flask('wtf')
app = Flask(__name__.split('.')[0])


@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200

#@app.route("/noticias/<pais>")
#def lista_de_noticias(pais):
#@app.route("/noticias")
#@app.route("/noticias/<pais>")
#@app.route("/noticias/<pais>/<estado>")
#def lista_de_noticias(pais=None, estado=None):
#    cat = request.args.get("categoria")
#    qtd = request.args.get("quantidade")
#    noticias = BD.query(pais=pais, categoria=cat).limit(qtd)
#    return render_template("lista_de_noticias.html", noticias=noticias), 200

@app.route("/<name>")
def index(name):
    if name.lower() == "elias":
        return "Olá {}".format(name), 200
    else:
        return "Not Found", 404

@app.route("/html_page/<nome>")
def html_page(nome):
    return render_template("html_page.html", nome=nome)

@app.route("/json")
def json_api():
    pessoas = [{"nome": "Bruno Rocha"},
               {"nome": "Arjen Lucassen"},
               {"nome": "Anneke van Giersbergen"},
               {"nome": "Steven Wilson"}]
    #response = make_response(json.dumps(pessoas))
    #response.content_type = "application/json"
    # ou
    # response.headers['Content-Type'] = "application/json"
    #return response
    #return json.dumps(pessoas), 200, {"Content-Type": "application/json"}
    return jsonify(pessoas=pessoas, total=len(pessoas))

@app.route("/show_config")
def show_config():
    querystring_args = request.args.to_dict()
    post_args = request.form.to_dict()
    return jsonify(
        debug=current_app.config.get('DEBUG'),
        args=querystring_args,
        vars=post_args
    )

@app.route("/change_photo")
def perfil():
    item_id = request.form.get('item_id')
    photo = request.files.get('photo')
    if item_id and photo:
        filename = secure_filename(photo.filename)
        file_path =os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        photo.save(file_path)
        banco_de_dados.get(item_id=item_id).update(photo_path=file_path)
    return "Imagem atualizada", 201

@app.route('/login')
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if valid_login(username, password):
        response = make_response("Hello! Welcome back!")
        response.set_cookie('username', username)
        response.set_cookie('user_hash', get_hash(username))
        ...
        return response
    else:
        abort(403)



app.run(debug=True, use_reloader=True)
