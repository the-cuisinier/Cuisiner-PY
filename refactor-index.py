import firebase_admin
from firebase_admin import credentials, firestore
import json


f = open("data.json")
data = json.load(f)

cred = credentials.Certificate("./credentials.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'index')

setIngredients = set()
errors = []

for i in data.keys():
	try:
		for item in data[i]["materials"]:
			setIngredients.add(item)
	except:
		print("Error in Dish ID", i)

print(len(setIngredients))
# try:
# 	doc_ref.document(u''+dataId+'').set(newDict)
# except Exception as e:
# 	print("Adding recipe", newDict["name"], "failed")
# 	errors.append(e)