from tkinter import *

root = Tk()

# creating an input label
label = Label(root, text='Enter your name? ')
e = Entry(root, width=50)

def onClick():
    name = e.get()
    label2 = Label(root, text=f'Your name is {name}').grid(row=3, column=1)

# Creating a Button
btn = Button(root, text='Click Me', command=onClick)
btn.grid(row=2, column=0)
label.grid(row=1, column=0)
e.grid(row=1, column=1)


# creating the event loop
root.mainloop()