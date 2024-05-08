from pathlib import Path
from tkinter import filedialog, Tk
from os import startfile

Tk().withdraw()

MY_PATH = Path(filedialog.askdirectory(title="Please select a folder..."))
#parent = MY_PATH.parent
#prep = Path(parent, "PREP")

prep = MY_PATH.parent / "PREP"
prep.mkdir(exist_ok=True)

startfile(prep)