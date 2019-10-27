from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import dataManipulation as dm

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    data = {"data":"Hello World"}
    return jsonify(data)


@app.route('/yo')
def hi():
    z = dm.fn()
    print("Yeet!",z)
    return jsonify(z)


if __name__ == "__main__":
    app.run()
