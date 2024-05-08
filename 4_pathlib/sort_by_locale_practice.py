from pathlib import Path
from tkinter import Tk, filedialog
import shutil

Tk().withdraw()

MY_FOLDER = Path(filedialog.askdirectory(title="Select folder..."))

RESULT = MY_FOLDER.parent / "RESULT"
RESULT.mkdir(exist_ok=True)

for f in MY_FOLDER.rglob("*.*"): #all files, including in subfolders
    locale_code = f.stem.split("_")[-1]
    destination_folder = RESULT / locale_code
    destination_folder.mkdir(exist_ok=True)
    shutil.copy2(f, destination_folder)