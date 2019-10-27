from flask import Flask
from flask import jsonify, request
from flask_cors import CORS, cross_origin
import dataManipulation as dm

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    data = {"data": "Hello World"}
    return jsonify(data)

#http://127.0.0.1:5000/search?q=AON Center
@app.route('/search')
def search():
    search_query = request.args.get('q')
    result = dm.get_info(search_query)
    print("Yeet!", result)
    return jsonify(result)


@app.route('/allBuildings')
def getAllBuildings():
    building_names = dm.getAllBuildingNames()
    print(type(building_names))
    return jsonify(building_names)


@app.route('/allBuildingsForReact')
def getAllBuildingsReact():
    building_names = dm.getAllBuildingNamesReact()
    print("flask :\n", building_names)
    data = {"data": building_names}
    return jsonify(building_names)


if __name__ == "__main__":
    app.run()
