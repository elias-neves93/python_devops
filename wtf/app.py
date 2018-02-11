from flask import Flask

app = Flask('wtf')
app = Flask(__name__.split('.')[0])

@app.route("/")
def hello_world():
    return "Hello World! <strong>I am learning Flask</strong>", 200

app.run()
