from tkinter import Tk, filedialog
from csv import DictReader

Tk().withdraw()

MY_FILE = filedialog.askopenfilename(title="Open csv file",
                                     filetypes=(("Comma Seperated Values","*.csv"),))

with open(MY_FILE, "r", encoding="utf-8", newline="") as csv_file:
    csv_reader = DictReader(csv_file, delimiter=",", quotechar='"')
    for row in csv_reader:
        print(row["Target Locale"], row["ICE Match"])