from flask import Flask, request
from flask import render_template
import utils
app = Flask(__name__)

# APIS
@app.route("/", methods=['POST'])
def guardar():
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    return {
        name: name,
        email: email,
        password: password
    }


@app.route("/", methods=['GET'])
@app.route("/<name>", methods=['GET'])
def home(name=None):
    last_name = request.args.get("last_name")
    return render_template('index.html', name=name)
