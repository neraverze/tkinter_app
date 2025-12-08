import os

IMAGE_EXTENSIONS = ['jpg', 'jpeg', 'png', 'bmp']


# getting the name of all of the files present with an extension of jpg
files_in_dir = os.listdir(os.path.dirname(os.getcwd()))
image_files = []
for file in files_in_dir:
    # splitting the extension
    try:
        name, extension = file.split(".")
        if extension in IMAGE_EXTENSIONS:
            image_files.append(file)
    except:
        pass

print(image_files)
