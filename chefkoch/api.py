import requests
from enum import Enum
from bs4 import BeautifulSoup
import re

"""With courtesy of https://raw.githubusercontent.com/florianschmidt1994/chefkoch-api/master/chefkoch.py"""


class RecipeNotFoundError(Exception):
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id


class OrderBy(Enum):
    relevance = 2
    rating = 3
    difficulty = 4
    max_time_needed = 5
    date = 6
    random = 7
    daily_shuffle = 8


class LogConfig:
    LOG_FILE = "log.txt"
    NUMBER_OF_RECIPIES = "number_of_recipies"
    OFFSET = "offset"


class ChefkochApi:
    """An API Wrapper for www.chefkoch.com"""

    def __init__(self):
        self.session = requests.session()
        self.is_logged_in = False

    def get_recipe(self, recipe_id):
        """Returns a recipe as a dict for a given recipe_id"""
        url = "https://api.chefkoch.de/v2/recipes/%s" % recipe_id
        res = self.session.get(url)
        if res.status_code is not 200:
            raise RecipeNotFoundError(recipe_id)
        else:
            return res.json()

    def search_recipe(
        self,
        query="",
        offset=0,
        limit=50,
        minimum_rating=0,
        maximum_time=0,
        order_by=OrderBy.relevance,
        descend_categories=1,
        order=0,
    ):
        """Returns a list of recipes that match the given search tearms"""
        payload = {
            "query": query,
            "limit": limit,
            "offset": offset,
            "minimumRating": minimum_rating,
            "maximumTime": maximum_time,
            "orderBy": order_by,
            "descendCategories": descend_categories,
            "order": order,
        }
        res = self.session.get("https://api.chefkoch.de/v2/recipes", params=payload)
        if res.status_code is not 200:
            raise ConnectionError("Response is not 200")
        else:
            return res.json()

    def get_rating_by_recipe_id(self, recipe_id, db):
        url = "http://www.chefkoch.de/rezepte/wertungen/" + recipe_id + "/"
        r = self.session.get(url)
        response = r.content.decode("utf-8")

        soup = BeautifulSoup(response, "html.parser")

        recipe_rating = {}
        recipe_rating["_id"] = recipe_id

        voting_table = soup.select(".voting-table tr")

        if not voting_table:
            recipe_rating["rating"] = []
            return recipe_rating

        voting_table.pop(0)

        votings = []
        for entry in voting_table:
            td = entry.select("td")

            voting_by_user = {}
            voting_by_user["voting"] = re.findall(
                r"\d+", td[0].select("span span")[0].get("class")[1]
            )[0]
            voting_by_user["name"] = td[1].text.strip()

            # check if user account was removed from chefkoch.de
            if td[1].select("a"):
                voting_by_user["id"] = td[1].select("a")[0].get("href").split("/")[3]
                # adds user to db
                # TODO: This logic should be in tasks.py
                self.add_unknown_user(voting_by_user["id"], db)
            else:
                voting_by_user["id"] = "unbekannt"
                print(voting_by_user)
                print(recipe_id)
                print(entry.text.strip())

            voting_by_user["date"] = td[2].text.strip()

            votings.append(voting_by_user)

        recipe_rating["rating"] = votings

        return recipe_rating
