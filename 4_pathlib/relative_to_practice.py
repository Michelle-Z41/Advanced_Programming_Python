from pathlib import Path
from tkinter import filedialog, Tk
from shutil import copy2

def remove_empty_folders(p: Path):
    if p.is_dir():
        contents = list(p.glob("*"))
        if len(contents) == 0: # if empty, delete the folder
            p.rmdir()
        else:
            for f in contents:
                remove_empty_folders(f) # recursive function
        
Tk().withdraw()

MY_FOLDER = Path(filedialog.askdirectory(title="Select folder..."))
RESULT = MY_FOLDER.parent / "RESULT" # / means plus path
RESULT.mkdir(exist_ok=True)

my_locales = set()

for f in MY_FOLDER.rglob("*.*"):
    locale_code = f.stem.split("_")[-1] # create a locale folder inside the RESULT folder
    local_folder = RESULT / locale_code
    local_folder.mkdir(exist_ok=True)
    my_locales.add(locale_code) # add the locale to the my_locales set

for f in MY_FOLDER.rglob("*"):
    if f.is_dir():
        # make the Android & iOS folder in each locale folder
        for local_code in my_locales:
            destination = Path(RESULT, local_code, f.relative_to(MY_FOLDER))
            destination.mkdir(exist_ok=True)
    if f.is_file():
        local_code = f.stem.split("_")[-1]
        destination = Path(RESULT, local_code, f.relative_to(MY_FOLDER))
        copy2(f, destination)

remove_empty_folders(RESULT)  