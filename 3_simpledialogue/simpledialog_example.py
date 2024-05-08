from tkinter import Tk, simpledialog

Tk().withdraw()

user_input = simpledialog.askstring(title="name", prompt="What's your name")

user_age = simpledialog.askinteger(title="Age", prompt="What's your age")

user_weight = simpledialog.askfloat(title="Weight", prompt="What's your weight in kg")

print(user_input, user_age, user_weight)