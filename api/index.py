from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from api.helper import forecast, corelation, corel
import json
import numpy as np


app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument("data")

class fore(Resource):
    def post(self):
        data = request.get_json(force=True)
        res = forecast(data["data"])
        return json.dumps(res)
    

class core(Resource):
    def post(self):
        json_data = request.get_json(force=True)

        #data_type = json_data["data_type"]
        #year_from = json_data["year_from"]
        #year_to = json_data["year_to"]
        data1 = np.array(json_data["data1"])
        data2 = np.array(json_data["data2"])

        features = []

        base =2010
        year_from = json_data["year_from"]
        year_to = json_data["year_to"]
        data_type = json_data["data_type"]

        f = (year_from-base)*data_type
        t = f+data_type+(year_to-year_from)*data_type

        for item in data1:
            features.append(np.array(item[f:t]))

        res = corel(features,data2)
        
        return json.dumps(res)
    
    

api.add_resource(fore,'/forecast')
api.add_resource(core,'/corelation')

if __name__ == '__main__':
    app.run(debug=True)