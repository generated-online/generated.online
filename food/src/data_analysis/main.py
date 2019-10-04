from data_analysis.analysis import DataAnalysis
from preprocess.data_handling import DataHandler

if __name__ == "__main__":
    data_analysis = DataAnalysis(DataHandler().read_data())

    data_analysis.draw_number_of_votes_vs_views()
    data_analysis.draw_number_of_votes_vs_ratings()
    data_analysis.draw_hist_ratings()
    data_analysis.draw_hist_views()
    data_analysis.draw_hist_views_cummulative()
    data_analysis.draw_views_vs_ratings()
