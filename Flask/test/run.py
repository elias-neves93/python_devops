# -*- coding: UTF-8 -*-

from flask import Flask,jsonify
from Blueprints.groups import groups
from Blueprints.users import users


app = Flask(__name__)
app.register_blueprint(groups)
app.register_blueprint(users)

@app.route("/")
def index():
    return "<h1> Response Flask </h1>"

if __name__ == "__main__":
    app.run(debug=True)
