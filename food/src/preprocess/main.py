from preprocess.data_handling import DataHandler

if __name__ == "__main__":
    d = DataHandler()
    d.concatenate_data_files()
    d.read_small_data()
    d.read_data()
