from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("File Opener")
root.geometry("400x400")

# checkboxes return 1s or 0s, where 1 is checked
result = IntVar()

my_lbl = Label(root)
def checked():
    my_lbl.config(text=result.get())

cb = Checkbutton(root, text='Check this', variable=result)
cb.pack()
Button(root, text='See Status', command=checked).pack()
my_lbl.pack()

root.mainloop()