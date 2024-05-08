from pathlib import Path
from tkinter import Tk, filedialog, simpledialog 
from os import startfile

Tk().withdraw()

f = Path(filedialog.asksaveasfilename(title="Save as...",
                                      filetypes=(("Text Files", "*.txt"),),
                                      defaultextension="*.txt"))

to_write = simpledialog.askstring(title="Ask user...", prompt="What to write?")
f.write_text(to_write, encoding="utf-8")
startfile(f)