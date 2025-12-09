from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title("File Opener")
lbl = Label(root)

def openFile():
    global my_img
    filename = filedialog.askopenfilename(initialdir=os.path.dirname(os.getcwd()), title='Select Image File to Open', filetypes=((".jpeg Files", "*.jpg"), ("All Files", "*.*")))
    # displaying the image in another window
    top = Toplevel()
    top.title("Image Viewer")
    
    # opening the image
    try:
        originalImage = Image.open(filename)
        originalImage.thumbnail((600, 600), resample=Image.Resampling.LANCZOS)
        my_img = ImageTk.PhotoImage(originalImage)
        Label(top, image=my_img).pack()
    except Exception:
        top.destroy()
        lbl.config(text='Unable to Open File')

# Displaying an Image by letting the user select an image
openFileBtn = Button(root, text='Select Image', command=openFile)
openFileBtn.pack()
lbl.pack()


root.mainloop()