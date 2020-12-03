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
doc_ref = db.collection(u'recipes')

errors = []

for i in data.keys():
	tempData = data[i]["name"]
	dataId = convertNameToId(tempData)
	try:
		doc_ref.document(u''+dataId+'').set(data[i])
	except Exception as e:
		print("Adding recipe", data[i]["name"], "failed")
		errors.append(e)