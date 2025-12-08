from tkinter import *

root = Tk()
root.title("Simple Calculator")

# creating the entry field
e = Entry(root, width=45, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

# displaying the numbers one by one on the entry field
def displayNum(number):
    # insert the current number at the end of the entry
    e.insert(END, str(number))

OPERANDS = []

# adding logic for the add button
def addBtnLogic():
    # adding the operands
    OPERANDS.append(int(e.get()))
    e.delete(0, END)

# showing the result
def showResult():
    # adding the current value
    OPERANDS.append(int(e.get()))

    # adding the values stored in operand
    sum = 0
    for num in OPERANDS:
        sum += num
    OPERANDS.clear()

    print(sum)
    # inserting the value into the entry field
    e.delete(0, END)
    e.insert(0, sum)

# adding logic for clearing the screen
def clearScreen():
    e.delete(0, END)
    # emptying the operands list
    OPERANDS.clear()

# creating the numeric buttons
numeric_btns = []
for i in range(0, 10):
    btn = Button(root, text=f"{i}", padx=35, pady=20, command=lambda i=i: displayNum(i))
    numeric_btns.append(btn)

# placing the numeric btns
rowStart = 1
for i in range(9, 0, -3):
    # running the column loop
    for j in range(2, -1, -1):
        numeric_btns[i - j].grid(row=rowStart, column= 2 - j, sticky='ew')
    rowStart += 1

# placing the zeroth button
numeric_btns[0].grid(row=rowStart, column=0, sticky='ew')

def negateBtnLogic():
    OPERANDS.append(int(f"-{e.get()}"))
    e.delete(0, END)
    return

def productBtnLogic():
    return

def slashBtnLogic():
    return


# placing the auxillary buttons
clearScBtn = Button(root, text='Clear', padx=35, pady=20, command=clearScreen).grid(row=rowStart, column=1, columnspan=2, sticky='ew')
rowStart += 1
addBtn = Button(root, text='+', padx=35, pady=20, command=addBtnLogic).grid(row=rowStart, column=0, sticky='ew')
equalBtn = Button(root, text='=', padx=35, pady=20, command=showResult).grid(row=rowStart, column=1, columnspan=2, sticky='ew')
rowStart += 1
minusBtn = Button(root, text='-', padx=35, pady=20, command=negateBtnLogic).grid(row=rowStart, column=0, sticky='ew')
productBtn = Button(root, text='*', padx=35, pady=20, command=productBtnLogic).grid(row=rowStart, column=1, sticky='ew')
slashBtn = Button(root, text='/', padx=35, pady=20, command=slashBtnLogic).grid(row=rowStart, column=2, sticky='ew')

# firing the main loop
root.mainloop()