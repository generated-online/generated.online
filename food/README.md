# General

Currently we are offering 3 parts for our food generation framework:

1. chefkoch: it's a crawler for the german recipe website chefkoch.de. You can start the
crawling process by running the [main.py](src/chefkoch/main.py). This process takes
about 4h. If it's interrupted due to any reason, just restart it, and the crawler picks
up its work where it left it. The data will be saved to src/data.
2. data_analysis: this module plots some graphs about the downloaded data. It assumes
that the data is located in src/data.
3. preprocess: mainly pre-processes the data (again assumes it's located in src/data).
But can also create word clouds and export it to a .txt file.
