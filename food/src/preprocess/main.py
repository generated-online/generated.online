from preprocess.data_handling import DataHandler
from preprocess.exporting import Exporter


def do_filtering():
    d = DataHandler()
    return d.get_filtered_data(
        [lambda x: x["rating"], lambda x: x["rating"]["numVotes"] >= 10],
        list(d.read_small_data()),
    )


if __name__ == "__main__":
    filtered_data = do_filtering()
    exporter = Exporter(filtered_data)
    print(exporter.get_formatted_text())
