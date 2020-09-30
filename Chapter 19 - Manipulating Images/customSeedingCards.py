#!python3
#customSeedingCards.py - Create invitations for a list of guests.

import os, sys
from PIL import Image, ImageDraw

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

os.makedirs('Invitations', exist_ok=True)

guestFile = open('guests.txt')
guestList = guestFile.readlines()
print(guestList)

catImg = Image.open('catlogo1.png')

for guest in guestList:
    imgObj = Image.new('RGBA', (288, 360), 'white')
    draw = ImageDraw.Draw(imgObj)
    #Draw border.
    draw.line([(0,0), (288,0), (288,360), (0,360), (0,0)], fill = 'black', width= 10)
    #Add text and image.
    draw.text((54, 50), 'Invitation for ' + guest, fill= 'black')
    imgObj.paste(catImg, (104,125), catImg)
    #Saving file.
    imgFile = 'invitation_' + guest.replace(' ', '') + '.png'
    print('Creating invitation for %s...' % guest)
    imgObj.save(os.path.join('Invitations', imgFile))


