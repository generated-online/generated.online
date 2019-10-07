from preprocess.data_handling import DataHandler
from preprocess.exporting import Exporter


def do_filtering(data=None):
    d = DataHandler()
    return d.get_filtered_data(
        [lambda x: x["rating"], lambda x: x["rating"]["numVotes"] >= 10], data
    )


def export_data(data):
    exporter = Exporter(data)
    with open("text.txt", "w") as f:
        f.write(exporter.get_formatted_text())


if __name__ == "__main__":
    export_data(do_filtering())
