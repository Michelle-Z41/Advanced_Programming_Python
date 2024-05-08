from pathlib import Path
from tkinter import Tk, filedialog

Tk().withdraw()

f = Path(filedialog.askopenfilename(title="Select file..."))
new_filename = f.stem + "_RENAMED" + f.suffix
new_filepath = f.with_name(new_filename)
f.rename(new_filepath)