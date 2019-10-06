from preprocess.data_handling import DataHandler


def do_filtering():
    d = DataHandler()
    d.get_filtered_data(
        [lambda x: x["rating"], lambda x: x["rating"]["numVotes"] >= 10]
    )


if __name__ == "__main__":
    do_filtering()
