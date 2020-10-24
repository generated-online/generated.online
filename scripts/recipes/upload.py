import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore as firestoreCloud
from  google.api_core.exceptions import NotFound
import re

# Use service account
cred = credentials.Certificate("generatedonline-a1cb0-firebase-adminsdk-ffohx-b8d5abe895.json")
firebase_admin.initialize_app(cred)
# define database
db = firestore.client()

with open('recipes/1_200.txt') as f:
    content = f.read()

content = content.replace("<|endoftext|>", "")
thingsToRemove = ['', "ml", 'l', 'mg', 'g', 'kg', 'und', 'für', 'cl', 'der', 'er', 'die', 'das', 'oder', 'n', '', 'el', 'tl', 'n', 'msp', 'großes', 'kleines', 'bund', 'kilo', 'gerieben', 'liter','schuss,' 'er','e', 's', 'kl', 'm', 'scheibe', 'ring', 'stück', 'stücke', 'prise', 'zehe', 'tasse', 'glas', 'becher', 'knolle', 'gehäuft', 'groß', 'große', 'klein', 'kleine', 'mittlere', 'pck', 'rot', 'rote', 'grüne', 'grün', 'gelb', 'dose', 'gemahlen', 'gestr', 'großer', 'italienischer', 'se', 'gehackt', 'edelsüß', 'zweig', 'großer', 'kleiner', 'heller', 'dl', 'saure', 'süße', 'stückige', 'stücke', 'gr', 'braun', 'frisch', 'gehackt', 'gemischt', 'pulver', 'tafeln', 'tafel', 'tube', 'type', 'tüte', 'cm', 'schwarze', 'schwarzer', 'passierte', 'passiert', 'zum', 'ungesüßt', 'davon', 'paket', 'form', 'in', 'mittelscharfer', 'rosenscharf', 'stange', 'stängel']

results = re.findall("={3}\s(.*)={3}\s*(=\s(([^=])*)\s=)*\s*(([=\s]{6}.*)*)\s*(.*):\s*(([^===])*)", content)

for result in results:
    ingredients = re.findall("=\s=\s=\s([^=]*)=\s=\s=\s*", result[4])
    if result[2] != '' and len(ingredients) and result[7] != '':
        data = {
            u'title': result[2],
            u'ingredients': ingredients,
            u'instructions': result[7]
        }        
        ref = db.collection('recipes').document()
        ref.set(data)

        for ingredient in ingredients:
            filtered = re.findall("([^/\\0-9.,-;:<>~+\(\)\[\]\s][^\s\\\/\(\)\[\],.]*)", ingredient)
            for f in filtered:
                if f.lower() not in thingsToRemove:
                    ingredientRef = db.collection('ingredients').document(f)
                    try:
                        ingredientRef.update({u'usedIn': firestoreCloud.ArrayUnion([ref.id])})
                    except NotFound:
                        ingredientRef.set({u'usedIn': firestoreCloud.ArrayUnion([ref.id])})

        print(f"Added: {data['title']}\n")
