import firebase_admin

from algoliasearch.search_client import SearchClient
from algoliasearch.configs import SearchConfig
from algoliasearch.search_client import SearchClient

import tqdm
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore as firestoreCloud
from  google.api_core.exceptions import NotFound
import re

def syncAlgoliaWith(data, id):
    ALGOLIA_ID = '7KL69V3MEL'
    ALGOLIA_ADMIN_KEY = 'ddb6ee365024a8e49fa0cdf86d5bb68e'
        
    config = SearchConfig(ALGOLIA_ID, ALGOLIA_ADMIN_KEY)
    config.batch_size = 1
    
    client = SearchClient.create_with_config(config)

    client._config.bach_size = 1

    # Add an 'objectID' field which Algolia requires
    data["objectID"] = id
    # Write to the algolia index
    index = client.init_index('Recipes')
    index.save_objects([data])

# Use service account
cred = credentials.Certificate("generatedonline-a1cb0-firebase-adminsdk-ffohx-b8d5abe895.json")
firebase_admin.initialize_app(cred)
# define database
db = firestore.client()

with open('recipes/1_200.txt') as f:
    content = f.read()

content = content.replace("<|endoftext|>", "")
thingsToRemove = ['cm', 'm', 'davon', 'de', 'dl', 'en', 'gr', 'frisch', 'gekörnte', "ml", 'l', 'mg', 'g', 'kg', 'und', 'für', 'cl', 'der', 'er', 'die', 'das', 'oder', 'n', '', 'el', 'tl', 'n', 'msp', 'großes', 'kleines', 'bund', 'kilo', 'gerieben', 'liter','schuss,' 'er','e', 's', 'kl', 'm', 'scheibe', 'ring', 'stück', 'stücke', 'prise', 'zehe', 'tasse', 'glas', 'becher', 'knolle', 'gehäuft', 'groß', 'große', 'klein', 'kleine', 'mittlere', 'pck', 'rot', 'rote', 'grüne', 'grün', 'gelb', 'dose', 'gemahlen', 'gestr', 'großer', 'italienischer', 'se', 'edelsüß', 'zweig', 'großer', 'kleiner', 'heller', 'dl', 'saure', 'süße', 'stückige', 'stücke', 'gr', 'braun', 'frisch', 'gehackt', 'gemischt', 'pulver', 'tafeln', 'tafel', 'tube', 'type', 'tüte', 'cm', 'schwarze', 'schwarzer', 'passierte', 'passiert', 'zum', 'ungesüßt', 'davon', 'paket', 'form', 'in', 'mittelscharfer', 'rosenscharf', 'stange', 'stängel', 'se']

results = re.findall("={3}\s(.*)={3}\s*(=\s(([^=])*)\s=)*\s*(([=\s]{6}.*)*)\s*(.*):\s*(([^===])*)", content)

for result in tqdm.tqdm(results):
    ingredients = re.findall("=\s=\s=\s([^=]*)=\s=\s=\s*", result[4])
    if result[2] != '' and len(ingredients) and result[7] != '':
        data = {
            u'title': result[2],
            u'ingredients': ingredients,
            u'instructions': result[7]
        }        
        ref = db.collection('algolia-test').document()
        ref.set(data)

        # for ingredient in ingredients:
        #     filtered = re.findall("([^/\\0-9.,-;:<>~+\(\)\[\]\s][^\s\\\/\(\)\[\],.]*)", ingredient)
        #     for f in filtered:
        #         if f.lower() not in thingsToRemove:
        #             ingredientRef = db.collection('ingredients').document(f.lower())
        #             try:
        #                 ingredientRef.update({u'usedIn': firestoreCloud.ArrayUnion([ref.id])})
        #             except NotFound:
        #                 ingredientRef.set({u'usedIn': firestoreCloud.ArrayUnion([ref.id])})
        
        syncAlgoliaWith(data, ref.id)

        print(f"Added: {data['title']}\n")