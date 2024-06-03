from csv import writer
from tkinter import Tk, filedialog

Tk().withdraw()

COLUM_HEADERS = ("Source Language", "Target Language", "Word Count")

ROWS = [
    ("English US", "Chinese PRC", 64),
    ("English UK", "Korean", 572),
    ("German Germany", "Italian", 2316),
    ("English US", "Russian", 165),
    ("English US", "Polish", 894)
]

MY_FILE = filedialog.asksaveasfilename(title="Save as...",
                                       filetypes=(("Comma Separated Values", "*.csv"),),
                                       initialfile="my_file.csv")

with open(MY_FILE, "w", encoding="utf-8", newline="") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(COLUM_HEADERS)
    csv_writer.writerows(ROWS)