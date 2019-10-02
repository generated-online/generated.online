import glob
import json
import os
import pickle
from json import JSONDecodeError
from typing import List

from tqdm import tqdm

from preprocess.main import MODULE_NAME


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
