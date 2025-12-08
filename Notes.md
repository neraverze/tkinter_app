# Python Tkinter

## Everything in tkinter is a widget. The buttons, windows, popups, everything is a widget. To initialize tkinter, 
    from tkinter import *
    
    root = Tk()

    # Creating the label
    myLabel = Label(root, text='Hello, World!')

    mylabel.pack()  # Places the label on the root screen

    # Creating an event loop
    