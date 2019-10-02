from joblib import delayed
from joblib import Parallel
from tqdm import tqdm

from chefkoch.api import ChefkochAPI
from chefkoch.file_store import FileStore


class Crawler:
    BATCH_SIZE = 100

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

    def start_crawling(self):
        try:
            progress_bar = tqdm(total=self.number_of_recipes - self.start_offset)
            current_offset = self.start_offset
            while current_offset < self.number_of_recipes:
                current_offset += self._crawl_batch(progress_bar, current_offset)
        except KeyboardInterrupt:
            pass

    def _crawl_batch(self, progress: tqdm, offset: int):
        diff = self.process_batch(self.ck_api, self.file_store, offset=offset)
        progress.update(diff)
        return diff

    def process_batch(
        self, chefkoch_api: ChefkochAPI, file_store: FileStore, offset: int = 0
    ):
        json_result = chefkoch_api.search_recipe(
            query="*", offset=offset, limit=self.BATCH_SIZE
        )
        recipes = json_result["results"]

        recipes = Parallel(n_jobs=12)(
            delayed(self.load_recipe)(i, chefkoch_api) for i in recipes
        )

        file_store.save_recipes(recipes, offset)
        file_store.update_status(offset + len(recipes))
        return len(recipes)

    def load_recipe(self, meta_recipe: dict, chefkoch_api: ChefkochAPI):
        id = meta_recipe["recipe"]["id"]
        recipe_text = chefkoch_api.get_recipe(id)
        meta_recipe["recipe"]["score"] = meta_recipe["score"]
        meta_recipe["recipe"]["text"] = recipe_text
        return meta_recipe["recipe"]
