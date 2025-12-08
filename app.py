from tkinter import *

# setting up the root and title
root = Tk()

e = Entry(root)
e.insert(0, 'Hello, How are you?')
e.pack()

def myClick():
    myLabel = Label(root, text='Look, Saumya I love You!')
    myLabel.pack()

# Creating a Button
btn = Button(root, text='Click Me', command=myClick, fg='#4bc020', bg='black')
btn.pack()


# creating the event loop
root.mainloop()