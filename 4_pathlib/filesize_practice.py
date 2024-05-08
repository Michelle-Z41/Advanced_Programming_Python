from pathlib import Path
from tkinter import filedialog, Tk

def convert_bytes(bytes_number):
    tags = ["Byte", "Kilobyte", "Megabyte", "Gigabyte", "Terabyte"]
    i = 0
    double_bytes = bytes_number
    while (i < len(tags) and bytes_number >= 1024):
            double_bytes = bytes_number / 1024.0
            i = i + 1
            bytes_number = bytes_number / 1024
    return str(round(double_bytes, 2)) + " " + tags[i]


Tk().withdraw()

total_size = 0
MY_FOLDER = Path(filedialog.askdirectory(title="Select a folder..."))
for f in MY_FOLDER.iterdir():
    f_size = f.stat().st_size
    total_size += f_size
converted_size = convert_bytes(total_size)
print(converted_size)