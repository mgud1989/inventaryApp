import flask
from flask import Flask, request, jsonify
from app import showAllDoc, finderOneDoc

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route ('/', methods = ['GET'])

def home():
    return "<h1>My API with Python Flask</h1><p>bueno la idea seria que esta api devuelva los datos de la BBD mongo inventario</p>"   

@app.route('/api/macbooks/all', methods = ['GET'])

def api_macbooks():
    allMacbooks = showAllDoc()
    return jsonify (allMacbooks)

@app.route('/api/macbooks/', methods = ['GET'])

def api_id():
    if '_id' in request.args:
        _id = "macbook_" + str(request.args['_id'])

    result = finderOneDoc("_id", _id)
     
    return jsonify (result)


app.run()