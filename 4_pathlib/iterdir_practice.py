from pathlib import Path
from tkinter import filedialog, Tk

Tk().withdraw()

MY_FOLDER = Path(filedialog.askdirectory(title="Select a folder..."))
print(f"Contents of folder {MY_FOLDER.name}...")
for f in MY_FOLDER.iterdir():
    print(f"{f.name=}")
    print(f"{f.stem=}")
    print(f"{f.suffix=}", end="\n\n")