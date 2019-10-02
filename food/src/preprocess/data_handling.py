import json
import pickle
from json import JSONDecodeError
from pathlib import Path
from typing import List

from tqdm import tqdm


class DataHandler:
    def __init__(self, data_folder: Path = None):
        if not data_folder:
            data_folder = Path(__file__).parent.parent / "data"
        self.data_folder = data_folder
        self.recipes_folder = data_folder / "recipes"
        self.concatenated_file = data_folder / "all_recipes.pkl"

    def concatenate_data_files(self):
        if not self.recipes_folder.exists():
            raise FileNotFoundError(
                "Folder with recipes not found. Did you ran the" "crawler?"
            )
        concatenated_list_of_recipes = []

        all_data_file_names = self.recipes_folder.glob("*.json")

        for data_file_name in tqdm(all_data_file_names):
            try:
                with open(data_file_name, "r") as data_file:
                    data_list = json.load(data_file)
                    concatenated_list_of_recipes += data_list
            except JSONDecodeError:
                print(f"couldn't load file {data_file_name}")

        with open(self.concatenated_file, "wb") as f:
            pickle.dump(concatenated_list_of_recipes, f)

    def read_data(self, data_file: Path = None) -> List[dict]:
        if not data_file:
            data_file = self.concatenated_file
        with open(data_file, "rb") as f:
            return pickle.load(f)

    def read_small_data(self) -> List[dict]:
        if not self.recipes_folder.exists():
            raise FileNotFoundError(
                "Folder with recipes not found. Did you ran the" "crawler?"
            )
        with open(self.recipes_folder / "data_000100.json", "r") as f:
            return json.load(f)
