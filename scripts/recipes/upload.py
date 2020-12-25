
# ALGOLIA CONFIG
from algoliasearch.search_client import SearchClient
from algoliasearch.configs import SearchConfig
from algoliasearch.search_client import SearchClient
import json

# with open('recipes/algolia_admin_key.json') as f:
with open('recipes/algolia_admin_key_2.json') as f:
    keyfile = json.load(f)

# ALGOLIA_ID = '7KL69V3MEL'
# ALGOLIA_ID = 'D6W68MPLE5'
ALGOLIA_ID = 'IFRMJQG34A'
ALGOLIA_ADMIN_KEY = keyfile["key"]

# FIREBASE
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud import firestore as firestoreCloud
from  google.api_core.exceptions import NotFound

# Use service account
cred = credentials.Certificate("recipes/generatedonline-a1cb0-firebase-adminsdk-ffohx-753457dbeb.json")
firebase_admin.initialize_app(cred)
# define database
db = firestore.client()

# Imports
import tqdm
import re

# helper
def syncAlgoliaWith(data, id, ingredients):
    config = SearchConfig(ALGOLIA_ID, ALGOLIA_ADMIN_KEY)
    config.batch_size = 1
    
    client = SearchClient.create_with_config(config)
    client._config.bach_size = 1

    # Add an 'objectID' field which Algolia requires
    data["objectID"] = id
    data["filtered_ingredients"] = ingredients
    # Write to the algolia index
    index = client.init_index('Recipes')
    index.save_objects([data])

def saveIngredients(ingredients, id):
    for ingredient in ingredients:
        ingredientRef = db.collection('ingredients').document(ingredient)
        try:
            ingredientRef.update({u'usedIn': firestoreCloud.ArrayUnion([id])})
        except NotFound:
            ingredientRef.set({u'usedIn': firestoreCloud.ArrayUnion([id])})

def uploadData(filename, start_idx=0, algolia=True, firebase=True):
    with open(filename) as f:
        recipe_list = json.load(f)
    print(len(recipe_list))
    for idx, recipe in enumerate(tqdm.tqdm(recipe_list[start_idx:])):
        try:                # Upload to firebase
            if firebase:
                recipeRef = db.collection("recipes").document(recipe["id"])
                doc = recipeRef.get()
                if not doc.exists:
                    recipeRef.set(recipe["data"])
                    # saveIngredients(data_dict["ingredients"], data_dict["id"])
            # upload to algolia
            if algolia:
                syncAlgoliaWith(recipe["data"], recipe["id"], recipe["ingredients"])
        except Exception as e:
            print(e)
            print(f"At {idx}")
            break
    print("Uploaded all items.")

def processRawFile(filename):
    import os.path
    if os.path.isfile(f"{filename}_filtered.json"):
        print("File already exists!")
        return
    ## Data processing
    thingsToRemove = ['cm', 'm', 'davon', 'de', 'dl', 'en', 'gr', 'frisch', 'gekörnte', "ml", 'l', 'mg', 'g', 'kg', 'und', 'für', 'cl', 'der', 'er', 'die', 'das', 'oder', 'n', '', 'el', 'tl', 'n', 'msp', 'großes', 'kleines', 'bund', 'kilo', 'gerieben', 'liter','schuss,' 'er','e', 's', 'kl', 'm', 'scheibe', 'ring', 'stück', 'stücke', 'prise', 'zehe', 'tasse', 'glas', 'becher', 'knolle', 'gehäuft', 'groß', 'große', 'klein', 'kleine', 'mittlere', 'pck', 'rot', 'rote', 'grüne', 'grün', 'gelb', 'dose', 'gemahlen', 'gestr', 'großer', 'italienischer', 'se', 'edelsüß', 'zweig', 'großer', 'kleiner', 'heller', 'dl', 'saure', 'süße', 'stückige', 'stücke', 'gr', 'braun', 'frisch', 'gehackt', 'gemischt', 'pulver', 'tafeln', 'tafel', 'tube', 'type', 'tüte', 'cm', 'schwarze', 'schwarzer', 'passierte', 'passiert', 'zum', 'ungesüßt', 'davon', 'paket', 'form', 'in', 'mittelscharfer', 'rosenscharf', 'stange', 'stängel', 'se']

    with open(filename) as f:
        content = f.read().replace("<|endoftext|>", "")

    results = re.findall("={3}\s(.*)={3}\s*(=\s(([^=])*)\s=)*\s*(([=\s]{6}.*)*)\s*(.*):\s*(([^===])*)", content)

    processed = []
    for result in tqdm.tqdm(results):
        ingredients_raw = re.findall("=\s=\s=\s([^=]*)=\s=\s=\s*", result[4])
        ingredients = set()
        # Filter ingredients
        for ingredient_raw in ingredients_raw:
            filtered = re.findall("([^/\\0-9.,-;:<>~+\(\)\[\]\s][^\s\\\/\(\)\[\],.]*)", ingredient_raw)
            for ingredient_filtered in filtered:
                if ingredient_filtered.lower() not in thingsToRemove:
                    ingredients.add(ingredient_filtered.lower().capitalize())

        if result[2] != '' and len(ingredients) and result[7] != '':
            data = {
                u'title': result[2],
                u'ingredients': ingredients_raw,
                u'instructions': result[7]
            }
            ref = db.collection('algolia-test').document()
            # data, ingrediets, ref.id
            processed.append({"data": data, "id": ref.id, "ingredients": list(ingredients)})

    with open(f"{filename}_filtered.json", 'w') as f:
        json.dump(processed, f, ensure_ascii=False)

def analyzeData(filename):
    from collections import Counter
    with open(filename) as f:
        recipe_list = json.load(f)
    # empty set
    allIngredients = []
    for idx, recipe in enumerate(tqdm.tqdm(recipe_list)):
        allIngredients += recipe["ingredients"]

    print(list(dict.fromkeys(sorted(allIngredients, key=Counter(allIngredients).get, reverse=True))))



if __name__ == "__main__":
    filename = 'recipes/1_200.txt'
    # processRawFile(filename)
    # analyzeData(filename + "_filtered.json")
    uploadData(filename + "_filtered.json", start_idx=3000, algolia=True, firebase=False)
