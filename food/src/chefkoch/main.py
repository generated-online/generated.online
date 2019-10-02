from chefkoch.api import ChefkochAPI
from chefkoch.crawler import Crawler
from chefkoch.file_store import FileStore

# def crawl():
#     file_store = FileStore()
#     c = ChefkochAPI()
#
#     if file_store.log_file_exists:
#         number_of_recipes, start_offset = file_store.read_status()
#     else:
#         j = c.search_recipe(query="*", limit=10e10)
#         number_of_recipes = j["count"]
#         number_of_recipes, start_offset = file_store.create_log_file(number_of_recipes)
#
#     progress = tqdm(total=number_of_recipes - start_offset)
#     current_offset = start_offset
#     while current_offset < number_of_recipes:
#         diff = current_offset
#         current_offset += process_batch(c, file_store, offset=current_offset)
#         progress.update(current_offset - diff)

if __name__ == "__main__":

    c = Crawler(FileStore(), ChefkochAPI())
    c.start_crawling()
