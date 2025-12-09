from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Message Boxes")

# getting the image address
address = os.path.dirname(os.getcwd()) 
files = os.listdir(address)
my_img = ImageTk.PhotoImage(Image.open(os.path.join(address, files[0])))

def clicked():
    # creating another window
    top = Toplevel()
    top.title("Saumya")
    Label(top, image=my_img).pack()
    Button(top, text='Quit', command=top.destroy).pack()

# adding a button
Button(root, text='Open Image', padx=40, pady=20, command=clicked).pack()



root.mainloop()