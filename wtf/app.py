from flask import Flask
from flask import render_template
import json
from flask import make_response
from flask import jsonify
from flask import request, current_app


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

app.run(debug=True, use_reloader=True)
