from tkinter import *
from PIL import ImageTk, Image
import os

# initializing the root
root = Tk()
root.title("Image Viewer")

# reading the list of images present in the folder
IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'bmp']
images = []
imageDir = os.path.dirname(os.getcwd())
files = os.listdir(os.path.dirname(os.getcwd()))
for file in files:
    try:
        name, extension = file.split(".")
        if extension in IMAGE_EXTENSIONS:
            filePath = os.path.join(imageDir, file)
            images.append(filePath)
    except Exception:
        pass

# resizes the image for better visibility
def resizeImage(img, width):
    image = Image.open(img)
    image.thumbnail((width, width), Image.Resampling.LANCZOS)
    return image


# reading the image at startup
label = Label(root)
status = Label(root, bd=1, relief=SUNKEN, anchor=E)
curr_image = 0
if (len(images) == 0):
    label.config(text='No Images Present In The Parent Directory')
else:
    # opening the first image present
    my_img = ImageTk.PhotoImage(resizeImage(images[curr_image], 600))
    label.config(image=my_img)
    status.config(text=f"Image {curr_image + 1} of {len(images)}")
    label.image = my_img


# # programming the buttons
def showPrevImage():
    global curr_image
    curr_image -= 1
    if curr_image < 0:
        curr_image = len(images) - 1
    
    # opening the image
    my_img = ImageTk.PhotoImage(resizeImage(images[curr_image], 600))
    label.config(image=my_img)
    status.config(text=f"Image {curr_image + 1} of {len(images)}")
    label.image = my_img

# # showing the next image
def showNextImage():
    global curr_image
    curr_image += 1
    if curr_image >= len(images):
        curr_image = 0
    
    # opening the image
    my_img = ImageTk.PhotoImage(resizeImage(images[curr_image], 600))
    label.config(image=my_img)
    status.config(text=f"Image {curr_image + 1} of {len(images)}")
    label.image = my_img


# # creating the buttons
leftBtn = Button(root, text="<<", command=showPrevImage)
rightBtn = Button(root, text=">>", command=showNextImage)
quitBtn = Button(root, text="Exit Program", command=root.quit)


# # positioning everything
label.grid(row=0, column=0, columnspan=3, sticky='ew')
leftBtn.grid(row=1, column=0, sticky='ew')
quitBtn.grid(row=1, column=1, sticky='ew')
rightBtn.grid(row=1, column=2, sticky='ew')
status.grid(row=2, column=0, columnspan=3, sticky='ew')


# main loop
root.mainloop()