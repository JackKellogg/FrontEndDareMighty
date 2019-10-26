from flask import Flask
from main import *
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello World"


@app.route('/yo')
def hi():
    z = fn()
    return z


if __name__ == "__main__":
    app.run()
