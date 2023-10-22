from flask import Flask,request,jsonify
import configparser
import json 
from pymongo import MongoClient

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://kaverigojre:<pass>@kaveri.k2boztx.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

#==============================Reading file===========================================================


def read_ConfigFile(read_ConfigFile,databaseURL):
    config = configparser.ConfigParser()
    config.read(read_ConfigFile)


    client = MongoClient(uri, server_api=ServerApi('1'))
    client = MongoClient(databaseURL)
    db = client['config_database']
              # Send a ping to confirm a successful connection
    try:
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
       print(e,"Incorrectpassword")

    for section in config.sections():
        collection = db[section]
        for option in config.options(section):
            data = {
                "key": option,
                "value": config.get(section, option)
            }
            collection.insert_one(data)


def Mongo_fetch(databaseURL):
    client = MongoClient(databaseURL)
    db = client['config_database']
    config_data = {}
    for collection_name in db.list_collection_names():
        config_data[collection_name] = {}
        for item in db[collection_name].find():
            config_data[collection_name][item["key"]] = item["value"]

    return config_data




#==============================creating FLask app===========================================================
app = Flask(__name__)

@app.route('/get_config', methods=['GET'])
def get_config():
    config_data = Mongo_fetch(databaseURL)
    return jsonify(config_data)
#==============================running FLask app===========================================================

if __name__ == '__main__':
    filepath = r"C:\Users\Kaver\Python_Assignment_1\configfile"
    databaseURL = "mongodb://localhost:27017/Kaveri"

    try:
        read_ConfigFile(filepath,databaseURL)
        print("Configuration File Parser Results:")
        app.run()
    except FileNotFoundError:
        print("Error: Configuration file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

