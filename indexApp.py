import flask
from flask import Flask, request, jsonify
from app import showAllDoc, finderOneDoc

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route ('/', methods = ['GET'])

def home():
    return "<h1>API with Python Flask mongo</h1>Welcome to the inventary<p></p>"   

@app.route('/api/macbooks/', methods = ['GET'])

def api_id():
    if '_id' in request.args:
        _id = "macbook_" + str(request.args['_id'])

        result = finderOneDoc("_id", _id)
    else:
        result = showAllDoc()
    return jsonify (result)


app.run()