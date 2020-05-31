# Praser for https://www.gesetze-im-internet.de/
import string
import requests
import re
from io import BytesIO
from zipfile import ZipFile
from tqdm import tqdm

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


main_url = "https://www.gesetze-im-internet.de/"
subfix_list = list(string.ascii_uppercase) + list(string.digits)[1:]

for suffix in tqdm(subfix_list):
    crawl_url = f"{main_url}Teilliste_{suffix}.html"

    url = f"https://www.gesetze-im-internet.de/Teilliste_{suffix}.html"
    r = requests.get(url)
    r.text
    xml_sub_urls = [f"{x[1:-10]}xml.zip" for x in re.findall(r'<p><a\shref=\".(\/.*)\"><', r.text)]

    for i, xml_url in tqdm(enumerate(xml_sub_urls)):
        zip_url = main_url+ xml_url
        download_url(zip_url, f"{suffix}_{i}.zip")
    #     download_url = (zip_url, f"./{suffix}.zip")
    # print(zip_url)
    # resp = requests.get(main_url+ xml_sub_urls[0]).content
    # with ZipFile(BytesIO(resp)) as my_zip_file:
    #     for contained_file in my_zip_file.namelist():
    #         # with open(("unzipped_and_read_" + contained_file + ".file"), "wb") as output:
    #         for line in my_zip_file.open(contained_file).readlines():
    #             print(line)
    #             # output.write(line)


