from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text='Look, Saumya I love You!')
    myLabel.pack()

# Creating a Button
btn = Button(root, text='Click Me', command=myClick, fg='#4bc020', bg='black')
btn.pack()


# creating the event loop
root.mainloop()