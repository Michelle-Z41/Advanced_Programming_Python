from tkinter import filedialog, Tk
from pathlib import Path

Tk().withdraw()

REPORT_FILE = filedialog.askopenfilename(title="Choose file",  
                                            initialdir=Path.cwd(), 
                                            filetypes=(("Text files", "*.txt"),))

# an empty string "" evaluates to False
if REPORT_FILE:
    print(REPORT_FILE)
else:
    print("The user clicked cancel.")
