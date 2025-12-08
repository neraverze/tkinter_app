from tkinter import *

root = Tk()
root.title("Radio Buttons")

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

# Building the radio buttons
index=0
for text, mode in MODES:
    Radiobutton(root, text=text, value=mode, variable=pizza).grid(row=0, column=index)
    index += 1

root.mainloop()