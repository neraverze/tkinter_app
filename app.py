from tkinter import *

root = Tk()
root.title("Frames")

# creating a menu bar
menuBar = LabelFrame(root)
menuBar.grid(row=0, column=0)

# adding menu buttons
fileBtn = Button(menuBar, text='File', padx=5)
editBtn = Button(menuBar, text='Edit', padx=5)
viewBtn = Button(menuBar, text='View', padx=5)
helpBtn = Button(menuBar, text='Help', padx=5)


# positioning the menu buttons
fileBtn.grid(row=0, column=0)
editBtn.grid(row=0, column=1)
viewBtn.grid(row=0, column=2)
helpBtn.grid(row=0, column=3)

root.mainloop()