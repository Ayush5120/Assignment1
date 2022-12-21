import pandas as pd
import copy

from flask import Flask, request, json, Response
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

CORS(app)

result ={}
class Mongo:
    def __init__(self, data):
        self.client = MongoClient("mongodb://localhost:27017/")  
      
        database = data['database']
        collection = data['collection']
        cursor = self.client[database]
        self.collection = cursor[collection]
        self.data = data
class PinCode(Resource):
     def get(self):
        args = request.args
        pin = str(args["pin"])
        ans = result[pin]
        set_data = copy.deepcopy(ans);
        city = set_data.pop()
        state = set_data.pop()

        return {"state": state, "city": city}
class Users(Resource):
    def get(self):
        args = request.args
        firstname = args['firstname']
        lastname  = args['lastname']
        pincode = args['pincode']
        city = args['city']
        state = args['state']
        data = {
            "database": "registration",
            "collection": "users",
        }
        mongo_obj = Mongo(data)
        mongo_obj.collection.insert_one({"Firstname": firstname,"Lastname": lastname, "Pincode": int(pincode), "City": city, "State": state})
          
        return "Entry Added"
@app.route('/forms')
def get_form():
    f = open("template.html", "r")
    form = f.read()
    print(form)
    return form
        
api.add_resource(PinCode, '/pincodes')
api.add_resource(Users,'/users')

if __name__ == '__main__':
    data = {
        "database": "registration",
        "collection": "users",
    }
    mongo_obj = Mongo(data)
    data = pd.read_csv('indiapincodefinal.csv') 
    data = data.to_dict()
    for i in range(0,len(data['pincode'])):
        pincode = str(data['pincode'][i])
        city = str(data['Districtname'][i])
        state = str(data['statename'][i])
        result[pincode] = {city, state}

    app.run(debug=True, port=5001, host='0.0.0.0')