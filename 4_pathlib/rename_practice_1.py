from pathlib import Path
from tkinter import Tk, filedialog

Tk().withdraw()

f = Path(filedialog.askopenfilename(title="Select a file..."))
new_filepath = Path(filedialog.asksaveasfilename(title="Rename as...",
                                                 initialdir=f.parent,
                                                 initialfile=f.name))
f.rename(new_filepath)