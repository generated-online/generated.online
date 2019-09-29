import json
import os


class FileStore:
    def __init__(self, folder: str = "data"):
        self.folder = folder
        if not os.path.exists(folder):
            os.makedirs(folder)

    def save_recipes(self, recipes: list, number: int):
        with open(f"{self.folder}/data_{number:06d}.json", "w") as f:
            json.dump(recipes, f)
