from tkinter import Tk, filedialog
from csv import reader

Tk().withdraw()

MY_FILE = filedialog.askopenfilename(title="Open csv file",
                                     filetypes=(("Comma Seperated Values","*.csv"),))

with open(MY_FILE, "r", encoding="utf-8", newline="") as csv_file:
    csv_reader = reader(csv_file,delimiter=",", quotechar='"')
    header_row = next(csv_reader)
    print(header_row, end="\n------------------------\n")
    for row in csv_reader:
        print(row)

    # rows = list(csv_reader)
    # my_cell = rows[0][2]
    # print(my_cell)