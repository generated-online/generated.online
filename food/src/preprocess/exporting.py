from typing import List


class Exporter:
    EOS = "<|endoftext|>"
    EOL = "\n"

    def __init__(self, data: List[dict]):
        self.data = data

    def get_formatted_text(self):
        """Format the data the exporter was initialized with."""

        formatted_text = f"\n".join(map(self._encode_recipe, self.data))
        return formatted_text

    def _encode_recipe(self, recipe_dict: dict):
        """Converts a recipe dict to trainable string."""

        recipe_string = ""

        # === title
        recipe_string += self._encode_title(recipe_dict["title"]) + self.EOL * 2

        # === ingredients
        recipe_string += (
            self._encode_ingredient_groups(recipe_dict["text"]["ingredientGroups"])
            + self.EOL
        )

        # === instructions
        recipe_string += self._instructions_to_string(
            recipe_dict["text"]["instructions"]
        )

        return recipe_string

    def _encode_title(self, _title: str) -> str:
        return f"= {_title} ="

    def _encode_ingredient_groups(self, _ingredient_groups: List[dict]) -> str:
        ingredient_groups_string = ""
        for group in _ingredient_groups:
            ingredient_groups_string += self._encode_ingredient_group(group)
        return ingredient_groups_string

    def _encode_ingredient_group(self, _ingredient_group: dict) -> str:
        """Encodes a ingredient group.

        If the group has a header the header is placed on top of the list of
        ingredients."""

        ingredient_group_string = ""
        if not _ingredient_group["header"].strip() == "":
            ingredient_group_string += (
                f"= = {_ingredient_group['header']} = ={self.EOL}"
            )
        for _ingredient in _ingredient_group["ingredients"]:
            ingredient_group_string += (
                f"= = = {self._encode_ingredient(_ingredient)} = = ={self.EOL}"
            )
        return ingredient_group_string

    @staticmethod
    def _encode_ingredient(_ingredient: dict) -> str:
        """Combines amount, unit and name of an ingredient to one string.

        If amount is empty or 0, amount and unit are ignored."""

        ingredient_string = ""

        # add amount and unit if necessary
        if _ingredient["amount"] and _ingredient["amount"] != 0:
            ingredient_string += (
                str(_ingredient["amount"]) + " " + _ingredient["unit"] + " "
            )

        # add name of ingredient
        ingredient_string += _ingredient["name"]

        return ingredient_string

    def _instructions_to_string(self, _instruction: str) -> str:
        return (
            f"Instructions:{self.EOL*2}"
            f"{_instruction.replace(',', ' ,').replace('.', ' .').replace('  ', ' ')}"
            f"{self.EOS}"
        )
