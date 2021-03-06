import flask, app
from flask import Flask, request, jsonify
from app import showAllDoc, finderOneDoc, insertOneDoc, deleteOneDoc, updateOneDoc

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route ('/', methods = ['GET'])

def home():
    return "<h1>API with Python Flask mongo</h1>Welcome to the inventary<p></p>"   

@app.route('/api/macbooks/', methods = ['GET'])

def api_macbooksAll():
    result=showAllDoc()
    return jsonify(result)

@app.route('/api/macbooks/<idName>', methods = ['GET'])

def api_macbooksId(idName):
    
    result = finderOneDoc("name", ('macbook_'+ str(idName)))
    return jsonify (result)

@app.route('/api/macbooks/insert/<userName>', methods = ['POST'])

def api_macbooksInsert(userName):
    if not request.json or not userName in request.json:
        400
    
    inserted = insertOneDoc(userName)
    return jsonify(inserted)

@app.route('/api/macbooks/delete/<idNumber>', methods = ['DELETE'])

def api_macbooksDelete(idNumber):
    deleteOneDoc('name',('macbook_'+ str(idNumber)))

    return jsonify({'deleted': name})

@app.route('/api/macbooks/update/<idNumber>/<newUser>', methods = ['PUT'])

def api_macbooksUpdate(idNumber,newUser):
    
    updateOneDoc({'name':('macbook_'+ str(idNumber))}, {'user':newUser})
    
    return jsonify({'status': 'updated'})
app.run()