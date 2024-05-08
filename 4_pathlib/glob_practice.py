from pathlib import Path
from tkinter import filedialog, simpledialog, Tk

Tk().withdraw()

count = 0
MY_FOLDER = Path(filedialog.askdirectory(title="Choose a folder..."))
for f in MY_FOLDER.rglob("*.xml"):
    print(f.name)
    count += 1

print(f"There are {count} xml files in {MY_FOLDER.name}")