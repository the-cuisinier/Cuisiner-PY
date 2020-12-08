import firebase_admin
from firebase_admin import credentials, firestore
import json


def convertNameToId(name):
	dataId = "-".join([i.lower() for i in name.split(" ")])
	return dataId


f = open("data.json")
data = json.load(f)

cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'dish-index')

errors = []

for i in data.keys():
	newDict = {}
	tempName = data[i]["name"]
	dataId = convertNameToId(tempName)
	newDict["name"] = tempName
	newDict["id"] = dataId
	newDict["source"] = data[i]["source"]
	try:
		newDict["materials"] = data[i]["materials"]
	except:
		print("materials key does not exist for document", i)
	newDict["tags"] = data[i]["tags"]
	try:
		doc_ref.document(u''+dataId+'').set(newDict)
	except Exception as e:
		print("Adding recipe", newDict["name"], "failed")
		errors.append(e)