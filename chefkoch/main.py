import json

from chefkoch.api import ChefkochApi
from chefkoch.api import LogConfig

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


def get_batch(chefkoch_api: ChefkochApi, offset: int = 0):
    json_result = chefkoch_api.search_recipe(query="*", offset=offset, limit=BATCH_SIZE)
    recipes = json_result["results"]
    upload_recipes_to_fire_base(recipes)
    update_status(offset + len(recipes))
    return len(recipes)


def upload_recipes_to_fire_base(recipes: list):
    pass


def restart_crawling_recipes():
    c = ChefkochApi()
    j = c.search_recipe(query="*", limit=10e10)
    number_of_recipes = j["count"]
    write_log_file(number_of_recipes)

    current_offset = 0
    while current_offset < number_of_recipes:
        get_batch(c, offset=BATCH_SIZE)
        current_offset += 100


def continue_crawling_recipies():
    c = ChefkochApi()
    number_of_recipes, current_offset = read_status()

    while current_offset < number_of_recipes:
        current_offset += get_batch(c, offset=current_offset)


if __name__ == "__main__":
    restart_crawling_recipes()
    # continue_crawling_recipies()
