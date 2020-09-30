#!python3
#identifyingPhotoFolders.py - Find folders that have at least 50$ photos in them that are
# larger than 500 x 500 pixels

import os, sys
from PIL import Image

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

userPath = input('Specify a path that you wanna search.')

for foldername, subfolders, filenames in os.walk(userPath):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        #Check if the extension isn't png or jpg.
        if not (filename.lower().endswith('.jpg') or filename.lower().endswith('.png')):
            numNonPhotoFiles += 1
            continue

        imgObj = Image.open(os.path.join(foldername, filename))
        width, height = imgObj.size

        #Check if width and height are larger than 500.
        if width > 500 and height > 500:
            #Image is large enough to be considered a photo.
            numPhotoFiles += 1
        else:
            #Image is too small to be a photo
            numNonPhotoFiles += 1
        
        #If more than half of files were photos,
        #print the absolute path of the folder
        if numPhotoFiles > numNonPhotoFiles:
            print(os.path.abspath(foldername))