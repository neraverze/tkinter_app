from tkinter import *

# setting up the root and title
root = Tk()

# Creating a label
myLabel = Label(root, text='Hello, World').grid(row=0, column=0)
myLabel2 = Label(root, text='I Love You Saumya').grid(row=1, column=1)
myLabel3 = Label(root, text='').grid(row=2, column=0)

# Positioning Using Grids
# myLabel.grid(row=0, column=0)
# myLabel3.grid(row=1, column=2)
# myLabel2.grid(row=1, column=5)


# creating the event loop
root.mainloop()