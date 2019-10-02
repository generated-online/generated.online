import glob
import json
import os
import pickle
import sys
from json import JSONDecodeError

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


def read_data(data_file: str = "data.pkl"):
    with open(data_file, "rb") as f:
        return pickle.load(f)


def read_small_data():
    filename = os.path.join(MODULE_NAME, "../chefkoch/data/data_000100.json")
    with open(filename, "r") as f:
        return json.load(f)


def draw_hist_views(data=read_small_data()):

    views = list(map(lambda x: x["text"]["viewCount"], data))

    plt.hist(views, log=True, bins=100)
    plt.show()


def draw_hist_ratings(data=read_small_data()):

    ratings = list(
        map(lambda x: x["rating"]["rating"], filter(lambda x: x["rating"], data))
    )

    print(f"Lost {len(data)-len(ratings)} data points!", file=sys.stderr)

    plt.hist(ratings, log=True, bins=100)
    plt.title("Chefkoch-recipes rating histogram")
    plt.xlabel("rating in stars")
    plt.ylabel("Number of recipes")
    plt.show()


if __name__ == "__main__":
    draw_hist_ratings(data=read_data())
    # draw_hist_ratings()
