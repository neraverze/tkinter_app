from tkinter import *

# setting up the root and title
root = Tk()
root.title("Simple Calculator")

# creating the entry field
e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_show():
    # inserting the value
    e.insert(0, "button_value")
    return
    

# creating the buttons
numericBtns = []
for i in range(0, 10):
    _ = Button(root, text=f'{i}', padx=40, pady=20, command=button_show)
    numericBtns.append(_)

# placing the buttons on the screen
rowStart = 3
for i in range(9, 0, -3):
    # placing the first button
    numericBtns[i - 2].grid(row=rowStart, column=0)
    numericBtns[i - 1].grid(row=rowStart, column=1)
    numericBtns[i].grid(row=rowStart, column=2)
    rowStart += 1

# placing the zeroth button
numericBtns[0].grid(row=rowStart, column=0)

# creating clear screen, equals and add button
clearSc = Button(root, text="Clear", padx=79, pady=20)
equalBtn = Button(root, text='=', padx=91, pady=20)
addBtn = Button(root, text='+', padx=39, pady=20)

# placing the auxillary buttons
clearSc.grid(row=rowStart, column=1, columnspan=2)
rowStart += 1
equalBtn.grid(row=rowStart, column=1, columnspan=2)
addBtn.grid(row=rowStart, column=0)

# firing the main loop
root.mainloop()