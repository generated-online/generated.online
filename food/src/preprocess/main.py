import re

import matplotlib.pyplot as plt
from wordcloud import WordCloud

from preprocess.data_handling import DataHandler


def _get_nested_dict_entry(source: dict, key_string: str):
    keys = re.findall(r"\w+", key_string)
    try:
        value = source
        for key in keys:
            value = value[key]
    except KeyError:
        raise KeyError(
            f"The keystring {key_string} ({keys}) could not be found in"
            f"the source dict ({source})."
        )
    return value


def select_interesting_stuff(item: dict):
    filtered_dict = {}
    filters = [
        ("id", "id"),
        ("title", "title"),
        ("preparationTime", "preparation_time"),
        ("rating", "rating"),
        ("score", "score"),
        ("text/cookingTime", "cooking_time"),
        ("text/ingredientGroups", "ingredient_groups"),
        ("text/ingredientsText", "ingredients_text"),
        ("text/instructions", "instructions"),
        ("text/restingTime", "resting_time"),
        ("text/servings", "servings"),
        ("text/subtitle", "subtitle"),
        ("text/tags", "tags"),
        ("text/totalTime", "total_time"),
        ("text/viewCount", "view_count"),
    ]
    for key_string_source, key_string_target in filters:
        filtered_dict[key_string_target] = _get_nested_dict_entry(
            item, key_string_source
        )
    return filtered_dict


def get_concatenated_text(data):
    # pattern = re.compile(r"\b(" + "|".join(stopwords) + ")\\W", re.I)
    words = " ".join(map(lambda x: x["text"]["instructions"], data))

    print("done doing words.")
    # words = pattern.sub("", words) # too slow
    return words


def do_word_cloud():
    d = DataHandler()
    data = d.get_filtered_data(
        [lambda x: x["rating"], lambda x: x["rating"]["numVotes"] >= 10]
    )

    text = get_concatenated_text(data)
    wordcloud = WordCloud(width=1920, height=1080, contour_color="white").generate(text)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


def do_filtering():
    d = DataHandler()
    d.get_filtered_data(
        [lambda x: x["rating"], lambda x: x["rating"]["numVotes"] >= 10]
    )


if __name__ == "__main__":
    do_filtering()
