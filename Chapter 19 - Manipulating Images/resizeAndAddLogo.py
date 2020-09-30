#!python3
#resizeAndAddLogo.py - Resize all images in current directory to fit in a 300x300 square
#and adds catlogo.png on the lower right corner.

import os, sys
from PIL import Image

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo1.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

#Loop over all files in the working directory.
os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
     or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) \
       or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself


    im = Image.open(filename)
    width, height = im.size 

    #Check if image needs to be resised.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        #Calculate the new width and height to resize to
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        #Resize image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))


    #Add the logo if the image looks good with it.
    if width < logoWidth * 2 or height < logoHeight * 2:
        print('skipping %s due to size concerns...' % filename)
    else:
        print('Adding logo to %s' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    #Save changes.
    im.save(os.path.join('withLogo', filename))
