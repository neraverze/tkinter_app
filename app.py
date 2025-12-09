from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("File Opener")
root.geometry("400x400")

# drop down menus
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

clicked = StringVar()
clicked.set("Monday")
drop = OptionMenu(root, clicked, *options)
drop.pack()
lbl = Label(root)
lbl.pack()

def show():
    lbl.config(text=clicked.get())

Button(root, text='Show Selection', command=show).pack()

root.mainloop()