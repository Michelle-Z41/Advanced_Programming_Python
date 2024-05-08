from pathlib import Path
from tkinter import Tk, filedialog
from os import startfile

Tk().withdraw()

f = Path(filedialog.askopenfilename(title="Open a file...",
                                    filetypes=(("Text Files", "*.txt"),)))

content = f.read_text(encoding="utf-8")
print(content)