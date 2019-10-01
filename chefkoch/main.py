import json

from joblib import delayed
from joblib import Parallel
from tqdm import tqdm

from api import ChefkochApi
from api import LogConfig
from file_store import FileStore

BATCH_SIZE = 100


def write_log_file(number_of_recipes: int):
    with open(LogConfig.LOG_FILE, "w") as log_file:
        json.dump({LogConfig.NUMBER_OF_RECIPIES: number_of_recipes}, log_file)


def update_status(offset: int):
    with open(LogConfig.LOG_FILE, "r") as log_file:
        data = json.load(log_file)
    data[LogConfig.OFFSET] = offset
    with open(LogConfig.LOG_FILE, "w") as log_file:
        json.dump(data, log_file)


def read_status():
    with open(LogConfig.LOG_FILE, "r") as log_file:
        data = json.load(log_file)
    return data[LogConfig.NUMBER_OF_RECIPIES], data[LogConfig.OFFSET]


def process_batch(chefkoch_api: ChefkochApi, file_store: FileStore, offset: int = 0):
    json_result = chefkoch_api.search_recipe(query="*", offset=offset, limit=BATCH_SIZE)
    recipes = json_result["results"]

    recipes = Parallel(n_jobs=12)(
        delayed(load_recipe)(i, chefkoch_api) for i in recipes
    )

    file_store.save_recipes(recipes, offset)
    update_status(offset + len(recipes))
    return len(recipes)


def load_recipe(meta_recipe: dict, chefkoch_api: ChefkochApi):
    id = meta_recipe["recipe"]["id"]
    recipe_text = chefkoch_api.get_recipe(id)
    meta_recipe["recipe"]["score"] = meta_recipe["score"]
    meta_recipe["recipe"]["text"] = recipe_text
    return meta_recipe["recipe"]


def restart_crawling_recipes():
    file_store = FileStore()
    c = ChefkochApi()
    j = c.search_recipe(query="*", limit=10e10)
    number_of_recipes = j["count"]
    write_log_file(number_of_recipes)

    current_offset = 0
    progress = tqdm(total=number_of_recipes)
    while current_offset < number_of_recipes:  # number_of_recipes:
        diff = current_offset
        current_offset += process_batch(c, file_store, offset=current_offset)
        progress.update(current_offset - diff)


def continue_crawling_recipies():
    file_store = FileStore()
    c = ChefkochApi()
    number_of_recipes, start_offset = read_status()

    progress = tqdm(total=number_of_recipes - start_offset)
    current_offset = start_offset
    while current_offset < number_of_recipes:
        diff = current_offset
        current_offset += process_batch(c, file_store, offset=current_offset)
        progress.update(current_offset - diff)


if __name__ == "__main__":
    # restart_crawling_recipes()
    continue_crawling_recipies()
