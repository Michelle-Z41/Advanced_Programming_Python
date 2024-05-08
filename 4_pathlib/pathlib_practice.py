from pathlib import Path
from tkinter import Tk, filedialog

Tk().withdraw()

f = Path(filedialog.askopenfilename(title="Select a file"))

print(f)
print(f.name)
print(f.stem)
print(f.suffix)
print(f.parent)
print(list(f.parents))