import json
import os


class FileStore:

    LOG_FILE = "log.txt"
    NUMBER_OF_RECIPIES = "number_of_recipes"
    OFFSET = "offset"

    def __init__(self, folder: str = None):
        if folder is None:
            folder = os.path.join(os.path.dirname(__file__), "../data")
        self.folder = folder

        if not os.path.exists(folder):
            os.makedirs(folder)

        self.log_file = os.path.join(folder, self.LOG_FILE)

        try:
            self.read_status()
            self.log_file_exists = True
        except FileNotFoundError:
            self.log_file_exists = False

    def save_recipes(self, recipes: list, number: int):
        """Write list of recipes as json file to disk in given folder (init)"""
        with open(f"{self.folder}/data_{number:06d}.json", "w") as f:
            json.dump(recipes, f)

    def create_log_file(self, number_of_recipes: int):
        """Create initial log file."""
        with open(self.log_file, "w") as log_file:
            json.dump(
                {self.NUMBER_OF_RECIPIES: number_of_recipes, self.OFFSET: 0}, log_file
            )

        return number_of_recipes, 0

    def update_log_file(self, offset: int):
        """Update current offset in log file"""
        with open(self.log_file, "r") as log_file:
            data = json.load(log_file)
        data[self.OFFSET] = offset
        with open(self.log_file, "w") as log_file:
            json.dump(data, log_file)

    def read_status(self):
        """Read current offset in log file"""
        with open(self.log_file, "r") as log_file:
            data = json.load(log_file)
        return data[self.NUMBER_OF_RECIPIES], data[self.OFFSET]
