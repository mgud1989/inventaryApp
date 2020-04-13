from pymongo import MongoClient


MONGO_URI = 'mongodb://localhost'
client = MongoClient(MONGO_URI, username = "root", password = 'admin')
db = client['inventary']
collection = db['macbooks']

countDoc = collection.count_documents({})
nextName = ("macbook_" + str(countDoc+1))

def insertOneDoc (user='undesigned'):
    doc = { "_id": nextName, "user" : user }
    collection.insert_one(doc)

    print ("inserted " + nextName)

def finderManyDoc (*dict): 
    results = collection.find(*dict)
    
    for r in results:
        print (r)
    
    return list(results)

def finderOneDoc (k, v):
    doc = {k : v}
    result = collection.find(doc)

    return list(result)

def updateOneDoc (keyFind, valueFind, keySet, valueSet):
    collection.update_many ({keyFind:valueFind},{'$set':{keySet:valueSet}})

def deleteOneDoc (k, v):
    doc = {k : v}
    collection.delete_one(doc)

def deleteManyDoc (k, v):
    doc = {k : v}
    collection.delete_many(doc)
    return print ('All ' + v + " has been deleted")

def showAllDoc():
    result = collection.find()

    return list(result)
