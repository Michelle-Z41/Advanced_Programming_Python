from csv import writer
from tkinter import Tk, filedialog

Tk().withdraw()

PIRATE_TEXT = "Pirate fire in the hole coxswain squiffy pinnace chase barkadeer Brethren of the Coast come about plunder. Davy Jones' Locker Pieces of Eight salmagundi main sheet keel mizzen run a shot across the bow yawl landlubber or just lubber chandler. Arr ballast mutiny long clothes to go on account scuppers topsail Sea Legs come about jolly boat. Port lad driver tackle gabion yawl wherry hempen halter bowsprit no prey, no pay. Yawl hardtack long boat marooned maroon hang the jib man-of-war matey strike colors come about. Hornswaggle pillage yardarm lugger mutiny snow heave down rum shrouds fluke. Barbary Coast weigh anchor rigging aft ho bounty Jolly Roger lugsail Shiver me timbers aye. Nipper case shot Sea Legs ballast sutler marooned Nelsons folly provost measured fer yer chains piracy. Fire in the hole six pounders crimp sheet jury mast starboard Nelsons folly Spanish Main salmagundi keelhaul."

COLUM_HEADERS = ("Sentence ID", "First five words","Sentence length", "Average word length")

ROWS = []

sentences = PIRATE_TEXT.split(".")
for row_number, sentence in enumerate(sentences, start=1):
    sentence = sentence.strip(" ")
    words = sentence.split(" ")
    first_five_words = " ".join(words[0:5])
    sentence_length = len(words)
    if sentence_length == 0:
        continue
    average_word_length = sum([len(word) for word in words]) / sentence_length
    my_row = (row_number, first_five_words, sentence_length, average_word_length)
    if average_word_length == 0:
        continue
    ROWS.append(my_row)

MY_FILE = filedialog.asksaveasfilename(title="Save as...",
                                       filetypes=(("Comma Separated Values", "*.csv"),),
                                       initialfile="my_file.csv")

with open(MY_FILE, "w", encoding="utf-8", newline="") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(COLUM_HEADERS)
    csv_writer.writerows(ROWS)