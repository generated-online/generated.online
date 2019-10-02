from joblib import delayed
from joblib import Parallel
from tqdm import tqdm

from chefkoch.api import ChefkochAPI
from chefkoch.file_store import FileStore


class Crawler:
    BATCH_SIZE = 100
    RECIPE_TEXT = "text"

    def __init__(self, file_store: FileStore, ck_api: ChefkochAPI):
        self.file_store = file_store
        self.ck_api = ck_api

        # if there is already a log file continue work by reading the total number of
        # recipes and the offset
        if self.file_store.log_file_exists:
            self.number_of_recipes, self.start_offset = file_store.read_status()
        else:
            # if there was no log file get the total number of recipes from the website
            # and set the offset to 0
            number_of_recipes = self.ck_api.search_recipe(query="*", limit=10e10)[
                "count"
            ]
            self.number_of_recipes, self.start_offset = file_store.create_log_file(
                number_of_recipes
            )

    def crawl(self):
        try:
            progress_bar = tqdm(total=self.number_of_recipes - self.start_offset)
            current_offset = self.start_offset
            while current_offset < self.number_of_recipes:
                delta = self._process_batch(current_offset)
                progress_bar.update(delta)
                current_offset += delta
        except KeyboardInterrupt:
            # could to interrupt handling like pulling the last batch or wait at
            # at most 10s
            pass

    def _process_batch(self, offset: int = 0) -> int:
        """Downloads a batch of recipes."""
        json_result = self.ck_api.search_recipe(
            query="*", offset=offset, limit=self.BATCH_SIZE
        )
        recipes = json_result["results"]

        recipes = Parallel(n_jobs=12)(
            delayed(self._load_recipe_text)(i) for i in recipes
        )

        self.file_store.save_recipes(recipes, offset)
        self.file_store.update_log_file(offset + len(recipes))
        return len(recipes)

    def _load_recipe_text(self, meta_recipe: dict) -> dict:
        """Downloads the instructions for one recipe."""
        id = meta_recipe["recipe"]["id"]
        recipe_text = self.ck_api.get_recipe(id)
        meta_recipe["recipe"]["score"] = meta_recipe["score"]
        meta_recipe["recipe"][self.RECIPE_TEXT] = recipe_text
        return meta_recipe["recipe"]
