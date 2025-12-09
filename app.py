from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("File Opener")
root.geometry("400x400")

# this var in setHorizontal is necessary for some reason
# which we don't know yet
# so let's stick with it while using sliders

def setHorizontal(var):
    vrt = vertical.get()
    horizontal.set(vrt)


# Sliders
vertical = Scale(root, from_=-100, to=200, command=setHorizontal)
horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
vertical.pack()
horizontal.pack()

# Creating a button to set horizontal bar equal to vertical bar
Button(root, text='Set Horizontal Bar', command=setHorizontal).pack()

root.mainloop()