import os
from copy import deepcopy

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


class FireStore:
    def __init__(self):

        dirname = os.path.dirname(__file__)
        credentials_filename = os.path.join(
            dirname, "generatedonline-a1cb0-firebase-adminsdk.json"
        )

        # Use a service account
        cred = credentials.Certificate(credentials_filename)
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

    def upload_recipes(self, recipes: list):
        batch = self.db.batch()
        for recipe in recipes:
            preprocessed_recipe = self.process_recipe_dict(recipe)
            doc_ref = self.db.collection(u"recipes").document(
                str(preprocessed_recipe["id"])
            )
            batch.set(doc_ref, preprocessed_recipe)
        batch.commit()

    def process_recipe_dict(self, recipe: dict):
        processed_recipe = deepcopy(recipe["recipe"])
        processed_recipe["score"] = recipe["score"]
        return processed_recipe
