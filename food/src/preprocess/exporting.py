from typing import List


class Exporter:
    def __init__(self, data: List[dict]):
        self.data = data

    def _reicpe_to_text(self, recipe_dict: dict):
        recipe = ""
        # headline filtering

        def clean_text(text: string):
            abbreviations = open("german_abbreviations.txt", "r").read()

            for word in text.split():
                if "." in abbreviations:
                    if word not in abbreviations:


        #def filter_headline(headline: string):

        recipe += "= " + recipe_dict["title"] + " =" + "\n"

        # ingredients
        def ingredient_to_string(_ingredient: dict):
            """Combines amount, unit and name to one string.

            If amount is empty or 0, amount and unit are ignored."""

            ingredient_string = ""

            # add amount and unit if necessary
            if ingredient["amount"] and ingredient["amount"] != 0:
                ingredient_string += (
                    str(ingredient["amount"]) + " " + ingredient["unit"] + " "
                )

            # add name of ingredient
            ingredient_string += ingredient["name"]

            return ingredient_string

        recipe += "\n"
        for group in recipe_dict["text"]["ingredientGroups"]:
            if not group["header"].strip() == "":
                recipe += "= = " + group["header"] + " ==\n"
            for ingredient in group["ingredients"]:
                recipe += f"= = = {ingredient_to_string(ingredient)} = = =\n"
        recipe += "\n"

        # instructions
        recipe += "Instructions:\n\n"
        recipe += recipe_dict["text"]["instructions"] + "\n"
        return recipe

    def get_formatted_text(self):
        formatted_text = f"\n".join(map(self._reicpe_to_text, self.data))
        return formatted_text

filter_text("asas")
