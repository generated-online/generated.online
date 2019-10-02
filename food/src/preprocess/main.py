from preprocess.data_handling import DataHandler

if __name__ == "__main__":
    # data = read_small_data()
    #
    # draw_hist_ratings(data=filter_none_ratings(data))
    #
    # draw_hist_views(data=data)
    #
    # draw_hist_views_cummulative(data=data)

    # draw_views_vs_ratings(data=filter_none_ratings(data))
    # draw_number_of_votes_vs_ratings(data=filter_none_ratings(data))
    # draw_number_of_votes_vs_views(data=filter_none_ratings(data))

    d = DataHandler()
    d.concatenate_data_files()
    d.read_small_data()
    d.read_data()
