from flask import Flask, jsonify, request
from app import server, mongo
from bson.objectid import ObjectId


@server.route('/', methods=['GET'])
def find():
    try:
        dbRequest = mongo.db.ontologies
    except:
        return jsonify({"message": "Not connected to database."}), 500
    ontologies = dbRequest.find()    
    output = []
    if not ontologies:
        return jsonify({"message": "No ontology found."})
    else:
        for ontology in ontologies:
            output.append({
            'type' : ontology['type'],\
            'functionalities' : ontology['functionalities']
            })
        return jsonify({'res' : output})


@server.route('/ontology/<string:type>', methods=['GET'])
def findByType(t):
    try:
        dbRequest = mongo.db.ontologies
    except:
        return jsonify({"message": "Not connected to database."}), 500
    output = []
    device = dbRequest.find_one({'type': t})
    if not ontology:
        return jsonify({"message": "No device found with the given ID."}), 404
    else:
        output.append({'_id' : str(device['_id']),\
            'type' : device['type'],\
            'functionalities' : device['functionalities']
            })
    return jsonify({'res' : output})

@server.route('/ontology/save', methods=['POST'])
def create():
    try:
        ontologies = mongo.db.ontologies
    except:
        return jsonify({"message": "Database connection impossible."}), 400
    try:
        new_ontology = devices.insert({
            'type': 'raspberry',\
            'functionalities':["getTemperature"]
        })
        data = ontologies.find_one({'_id': new_ontology})
        output = []
        output.append({'_id' : str(data['_id']),\
            'type' : data['type'],\
            'functionalities': data['functionalities']
        })
        return jsonify({"res": output[0], "message": "Ontology added successfully."})
    except:
        return jsonify({"message": "Something went wrong."}), 400
