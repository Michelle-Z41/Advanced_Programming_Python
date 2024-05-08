from tkinter import messagebox, Tk

Tk().withdraw()

current_resident = messagebox.askyesno(title="Current resident", message="Are you a current resident?")

if current_resident:
    community_service = messagebox.askyesno(title="Community service", message="Have you done community service?")

    if community_service:
        messagebox.showinfo(title="Congratulation!", message="Great! You're eligible for a prize!")