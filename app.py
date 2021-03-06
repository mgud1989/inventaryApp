from pymongo import MongoClient


MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI, username = "root", password = 'admin')
db = client['inventary']
collection = db['macbooks']

counterDoc = collection.count_documents({})

def insertOneDoc (user='undesigned'):
    global counterDoc 
    nextName = ("macbook_" + str(counterDoc+1))
    doc = { "name": nextName, "user" : user }
    collection.insert_one(doc)
    counterDoc+=1

    return finderOneDoc('name', nextName)

def finderManyDoc (*dict): 
    results = collection.find(*dict, {'_id':False})
    
    for r in results:
        print (r)
    
    return list(results)

def finderOneDoc (k, v):
    doc = {k : v}
    result = collection.find(doc, {'_id':False})

    return list(result)

def updateOneDoc (filter,newValue):
    
    collection.update_many (filter,{'$set':newValue})

def deleteOneDoc (k, v):
    doc = {k : v}
    collection.delete_one(doc)

def deleteManyDoc (k, v):
    doc = {k : v}
    collection.delete_many(doc)

def showAllDoc():
    result = collection.find({}, {'_id':False})

    return list(result)

updateOneDoc({'user':'kim'}, {'user':'kimberly'})