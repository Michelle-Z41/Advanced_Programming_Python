from pathlib import Path
from tkinter import Tk, filedialog, simpledialog

Tk().withdraw()

LANGUAGE_DICT = {
    "Target-Korean - UTF8" : "ko",
    "Target-Portuguese (Brazil) - UTF8" : "pt_BR",
    "Target-Russian - UTF8" : "ru",
    "Target-Arabic (Egypt) - UTF8": "ar",
    "Target-Farsi - UTF8": "fa",
    "Target-French (France) - UTF8": "fr",
    "Target-Polish - UTF8": "po",
    "Target-Russian - UTF8": "ru",
    "Target-Spanish (Latin America) - UTF8": "es_LA",
    "Target-Ukrainian - UTF8": "uk",
    "Target-Vietnamese - UTF8": "vi"
    }

MY_DIRECTORY = Path(filedialog.askdirectory(title="Select directory..."))
for language_directory in MY_DIRECTORY.iterdir():
    locale = LANGUAGE_DICT.get(language_directory.name)
    if locale is None:
        locale = simpledialog.askstring(title="Unmapped language", prompt="What locale code?")
    for f in language_directory.rglob("*.*"): # only matches files
        if f.stem.endswith("_" + locale):
            continue
        new_filename = f.stem + "_" + locale + f.suffix
        new_filepath = f.with_name(new_filename)
        f.rename(new_filepath)