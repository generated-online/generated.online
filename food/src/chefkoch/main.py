from chefkoch.api import ChefkochAPI
from chefkoch.crawler import Crawler
from chefkoch.file_store import FileStore

if __name__ == "__main__":

    c = Crawler(FileStore(), ChefkochAPI())
    c.start_crawling()
