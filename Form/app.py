import pandas as pd

from flask import Flask, request, json, Response
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

from pymongo import MongoClient
from bson.json_util import dumps

app = Flask(__name__)
api = Api(app)

CORS(app)

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
        pin = args["pin"]
        data = {
            "database": "registration",
            "collection": "pincode",
        }
        mongo_obj = Mongo(data)
        result = mongo_obj.collection.find_one({"pincode": int(pin)})
        return {"state": result["state"], "city": result["city"]}
    
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
            "collection": "pincode",
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
        "collection": "pincode",
    }
    mongo_obj = Mongo(data)

    data = pd.read_csv('indiapincodefinal.csv') 
    data = data.to_dict()  
    for i in range(0,len(data['pincode'])):
        mongo_obj.collection.insert_one({"pincode": data['pincode'][i],"city": data['Districtname'][i], "state": data['statename'][i]})
    
    app.run(debug=True, port=5001, host='0.0.0.0')