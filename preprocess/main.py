import glob
import json
import os
import pickle
import sys
from json import JSONDecodeError
from typing import List

import numpy as np
from matplotlib import pyplot as plt
from tqdm import tqdm

MODULE_NAME = os.path.dirname(__file__)


def concatenate_data_files(
    data_folder: str = "../chefkoch/data", output_file: str = "data.pkl"
):
    concatenated_list = []

    all_data_file_names = glob.glob(data_folder + "/*.json")

    for data_file_name in tqdm(all_data_file_names):
        try:
            with open(data_file_name, "r") as data_file:
                data_list = json.load(data_file)
                concatenated_list += data_list
        except JSONDecodeError:
            print(f"couldn't load file {data_file_name}")

    with open(output_file, "wb") as f:
        pickle.dump(concatenated_list, f)


def read_data(data_file: str = "data.pkl") -> List[dict]:
    with open(data_file, "rb") as f:
        return pickle.load(f)


def read_small_data() -> List[dict]:
    filename = os.path.join(MODULE_NAME, "../chefkoch/data/data_000100.json")
    with open(filename, "r") as f:
        return json.load(f)


def filter_none_ratings(data: List[dict]) -> List[dict]:
    """Remove data points that contain no rating."""

    filtered_data = list(filter(lambda x: x["rating"], data))
    recipes_lost = len(data) - len(filtered_data)
    print(
        f"Lost {recipes_lost} data points! ({recipes_lost/len(data)*100}%)",
        file=sys.stderr,
    )
    return filtered_data


def draw_hist(data, title: str, xlabel: str, ylabel: str, log: bool, *args, **kwargs):
    plt.hist(data, log=log, bins=100, *args, **kwargs)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()


def draw_hist_views(data=None, log: bool = True):
    if data is None:
        data = read_small_data()

    views = list(map(lambda x: x["text"]["viewCount"], data))

    draw_hist(
        views,
        f"Chefkoch-recipes views histogram{' (logarithmic scale)' if log else ''}",
        "Number of recipes",
        "number of views",
        log=log,
    )


def draw_hist_ratings(data=None, log: bool = True):
    if data is None:
        data = filter_none_ratings(read_small_data())

    ratings = list(map(lambda x: x["rating"]["rating"] if x["rating"] else -1, data))

    draw_hist(
        ratings,
        f"Chefkoch-recipes rating histogram{' (logarithmic scale)' if log else ''}",
        "rating in stars",
        "Number of recipes",
        log=log,
    )


def draw_hist_views_cummulative(data=None):
    if data is None:
        data = read_small_data()

    views = list(map(lambda x: x["text"]["viewCount"], data))

    """
    1. sort data:
        0 0 0 1 2 2 1000
        0 1 2 3 4 5    6
    2. cummulative
        0 0 0 1 3 5 1005
        0 1 2 3 4 5    6
    3. devide by max
    """

    views.sort()
    views = np.asarray(views, dtype=np.float)
    views /= views[-1]
    views = 1 - views
    views = np.flip(views) * 100

    plt.plot(np.linspace(0, 100, num=len(views)), views)
    plt.title("Cumulative percentage of views vs % recipes")
    plt.xlabel("% of recipes")
    plt.ylabel("% of views")
    plt.show()


if __name__ == "__main__":
    data = read_data()
    # data = read_small_data()

    draw_hist_ratings(data=filter_none_ratings(data))

    draw_hist_views(data=data)

    draw_hist_views_cummulative(data=data)
