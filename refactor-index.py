import firebase_admin
from firebase_admin import credentials, firestore
import json


def convertNameToId(name):
	dataId = "-".join([i.lower() for i in name.split(" ")])
	return dataId


def checkingErrorPercentage(key, keySpelling):
	if key in keySpelling or keySpelling in key:
		if len(key) > len(keySpelling):
			count = 0
			for i in range(len(key)):
				if key[i] == keySpelling[i]:
					count = count + 1
			print(count / len(key))
			if count / len(key) < 0.12:
				return True
			else:
				return False
		else:
			count = 0
			for i in range(len(keySpelling)):
				if key[i] == keySpelling[i]:
					count = count + 1
			print(count / len(keySpelling))
			if count / len(keySpelling) < 0.12:
				return True
			else:
				return False
	else:
		return False


f = open("data.json")
data = json.load(f)

cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'index')

setIngredients = {}
errors = []

for i in data.keys():
	try:
		for item in data[i]["materials"]:
			try:
				setIngredients[item]["recipes"].append(convertNameToId(data[i]["name"]))
			except:
				setIngredients[item] = {
					"recipes": [convertNameToId(data[i]["name"])]
				}
	except:
		error = True

# print(len(setIngredients))
# print(setIngredients)

for i in setIngredients:
	try:
		doc_ref.document(u''+i+'').set(setIngredients[i])
	except Exception as e:
		print(e)


