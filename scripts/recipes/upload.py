import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import re

# Use service account
cred = credentials.Certificate("generatedonline-a1cb0-firebase-adminsdk-ffohx-b8d5abe895.json")
firebase_admin.initialize_app(cred)
# define database
db = firestore.client()

with open('recipes/1_200.txt') as f:
    content = f.read()

content = content.replace("<|endoftext|>", "")

results = re.findall("={3}\s(.*)={3}\s*(=\s(([^=])*)\s=)*\s*(([=\s]{6}.*)*)\s*(.*):\s*(([^===])*)", content)

for result in results:
    intrigents = re.findall("=\s=\s=\s([^=]*)=\s=\s=\s*", result[4])
    if result[2] != '':
        data = {
            u'title': result[2],
            u'intrigents': intrigents,
            u'instructions': result[7]
        }        
        db.collection(u'firstTest').document().set(data)
        # print(data)
        print(f"Added: {data['title']}\n")
