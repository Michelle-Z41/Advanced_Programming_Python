import re

FILENAMES = [
"to-my_en_folder_dir_de-DE.csv",
"to-my_en_folder_dir_en-us.csv",
"to-my_en_folder_dir_es-LA.csv",
"to-my_en_folder_dir_es-MX.csv",
"to-my_en_folder_dir_es_ES.csv",
"to-my_en_folder_dir_fr-ca.csv",
"to-my_en_folder_dir_fr_FR.csv",
"to-my_en_folder_dir_it.csv",
"to-my_en_folder_dir_ja.csv",
"to-my_en_folder_dir_pt_BR.csv",]

PATTERN = r"_(\w{2}[-_]?(:?[\w]{2})?)\."

for filename in FILENAMES:
    match = re.search(PATTERN, filename)
    if match:
        print(filename)
        print(match.group(0))
        print(match.group(1))
        print()
    else:
        print("No match.", filename)