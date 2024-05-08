import re

filenames = ["20220225-6171-6219778b5fb13-My_Project_Strings-2022-02-26-01-42-51-offline.zip",
             "20220227-3031-62196b47df8df-Document_Translation-2022-02-27-00-50-31-offline.zip",
             "3029-62199837f9d82-Android_iOS_localization_pack-2022-02-27-13-11-23-offline.zip",
             "20220228-3036-2938gnd91nfdk-2022-02-28-12-13-23-offline.zip",
             "20220301-3030-29gn48fj72bsf-Revisions_to_localizations-2022-03-01-14-12-24-offline"]

PATTERN = re.compile(r"(\d{8})?-?\d{4}-\w{13}-(\w+)?-?\d{4}-[^\.]*(\..*)?")

for filename in filenames:
    match = re.search(PATTERN, filename)
    small_name = ""
    if match is None:
        small_name = input(f"No match for {filename}\nWhat is the small filename? ")
    else:
        if match.group(1) is None:
            datestamp = input(f"No datestamp for {filename}\nWhat is the datestamp? ")
        else:
            datestamp = match.group(1)
        if match.group(2) is None:
            name = input(f"No name for {filename}\nWhat is the name? ")
        else:
            name = match.group(2)
        if match.group(3) is None:
            ext = input(f"No extension for {filename}\nWhat is the extension? ")
        else:
            ext = match.group(3)
        small_name = datestamp + "_" + name + ext

    print("Small filename:", small_name, end="\n\n")