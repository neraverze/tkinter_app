from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")

# showinfo, showerror, showwarning, askokcancel, askyesno, askquestion (same as yes no)

def popup():
    answer = messagebox.askquestion("Info Box", "I Love You Saumya")
    print(answer)

# returns True or False depending upon the yes no clicked or ok cancel clicked

Button(root, text='Popup', command=popup).pack()
Button(root, text='Quit', command=root.quit).pack(anchor=E)

root.mainloop()