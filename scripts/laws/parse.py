import re
from pathlib import Path
from zipfile import ZipFile
from tqdm import tqdm


def get_files(data_path, file_type):
    """Returns all .filetype filenames of data_path folder
    :param file_type: e.g. .jpg
    :param data_path: path of folder to search for images
    """
    p = Path(data_path).glob('**/*')
    files = [x for x in p if x.is_file() and str(x).endswith(file_type)]

    if len(files) == 0 or files is None:
        print(f"No {file_type} files found in location {data_path}\n")
        return
    return files


# all_files = get_files("out/", ".zip")
# for zfile in tqdm(all_files):
#     with ZipFile(zfile, 'r') as zip_ref:
#         zip_ref.extractall("extracted/")

all_files = get_files("extracted/", ".xml")
all_txt = ""

for xmlfile in tqdm(all_files):
    with open(xmlfile, 'r') as f:
        data = f.read()
    cleaned = re.sub(r'\n+', '\n', re.sub(r'<[^>]*>', '\n', data))
    all_txt += (f"\n\n{cleaned}")

with open("result.txt", "w") as f:
    f.write(all_txt)
    