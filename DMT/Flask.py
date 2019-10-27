from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
from main import *
app = Flask(__name__)
CORS(app)

@app.route('/')

def home():
    data = {"data":"Hello World"}
    return jsonify(data)


@app.route('/yo')
def hi():
    z = fn()
    return z


if __name__ == "__main__":
    app.run()
