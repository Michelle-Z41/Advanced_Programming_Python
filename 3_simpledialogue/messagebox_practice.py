from tkinter import messagebox, Tk

Tk().withdraw()

messagebox.showinfo(title="showinfo", message="Successfully logged in.")
messagebox.showwarning(title="showwarning", message="You are not logged in.")
messagebox.showerror(title="showerror", message="Could not connect to the server.")

askquestion_result = messagebox.askquestion(title="askquestion", message="Import another file?")
askokcancel_result = messagebox.askokcancel(title="askokcancel", message="All files in this folder will be deleted.")
askretrycancel_result = messagebox.askretrycancel(title="askretrycancel", message="Do you wish to retry with a different file?")
askyesno_result = messagebox.askyesno(title="askyesno", message="Run program in safe mode?")
askyesnocancel_result = messagebox.askyesnocancel(title="askyesnocancel", message="Save a copy of all files?")

print(f"{askquestion_result=} {askokcancel_result=} {askretrycancel_result=} {askyesno_result=} {askyesnocancel_result=}")