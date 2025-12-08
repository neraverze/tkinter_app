# Python Tkinter

## Everything in tkinter is a widget. The buttons, windows, popups, everything is a widget. To initialize tkinter, 
    from tkinter import *
    
    root = Tk()

    # Creating the label
    myLabel = Label(root, text='Hello, World!')

    mylabel.pack()  # Places the label on the root screen

    # Creating an event loop
    root.mainloop()

Doing everything in tkinter is a two step process. You first create the widget and then place the widget on the screen.