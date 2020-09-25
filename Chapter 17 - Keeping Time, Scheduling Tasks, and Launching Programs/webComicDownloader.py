#!python3
#webComicDownloader.py - checks some web comics and downloads the images if the comic was updated.
# comic sites: left-handed toons, savageChickens, lunarBaboon.
import os, requests, bs4, threading, sys

print('Start of program.')

#Change directory to current working directory
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

os.makedirs('comicDownloaded', exist_ok=True) #Creates a folder to store the comics.




def downloadLeftHand():
    res = requests.get('http://www.lefthandedtoons.com')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('.comicimage')
    if comicElem == []:
        print('Could not find a image')
    else:
        comicUrl = comicElem[0].get('src')
        #check if the image that you wanna download already exists. If so, skip.
        if os.path.exists(os.path.join('comicDownloaded', os.path.basename(comicUrl))):
            print('You already have that image from Left-Handed, I ain\'t downloading that for you again.')
        else:
            print('Downloading image...%s' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            #Saving the image to comicDownloaded.
            imageFile = open(os.path.join('comicDownloaded', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100_000):
                imageFile.write(chunk)
            imageFile.close()

def downloadSavageChickens():
    res = requests.get('https://www.savagechickens.com')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('.entry_content img')
    if comicElem == []:
        print('Could not find image.')
    else:
        comicUrl = comicElem[0].get('src') #comicElem[0] means: get the first src from the element.
        #check if the image that you wanna download already exists. If so, skip.
        if os.path.exists(os.path.join('comicDownloaded', os.path.basename(comicUrl))):
            print('You already have that image from SavageChickens, I ain\'t downloading that for you again.')
        else:
            print('Downloading image...%s' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            #Saving the image to comicDownloaded.
            imageFile = open(os.path.join('comicDownloaded', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100_000):
                imageFile.write(chunk)
            imageFile.close()

def downloadLunarBaboon():
    res = requests.get('http://www.lunarbaboon.com')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comicElem = soup.select('#item36309886 > div:nth-child(3) > div:nth-child(3) > p:nth-child(1) > span:nth-child(1) > span:nth-child(1) > img:nth-child(1)')
    if comicElem == []:
        print('Could not find image')
    else:
        comicUrl = comicElem[0].get('src')
        comicLink = 'http://www.lunarbaboon.com'+ comicUrl
        if os.path.exists(os.path.join('comicDownloaded', os.path.basename(comicLink) + '.jpg')):
            print('You already have that image from LunarBaboon. I ain\'t downloading it again.')
        else:
            print('Downloading image...%s' % (comicLink))
            res = requests.get(comicLink)
            res.raise_for_status

            #Saving the image to comicDownloaded.
            imageFile = open(os.path.join('comicDownloaded', os.path.basename(comicLink) + '.jpg'), 'wb')
            for chunk in res.iter_content(100_000):
                imageFile.write(chunk)
            imageFile.close()


    
leftHandThread = threading.Thread(target=downloadLeftHand)
leftHandThread.start()

savageThread = threading.Thread(target=downloadSavageChickens)
savageThread.start()

baboonThread = threading.Thread(target=downloadLunarBaboon)
baboonThread.start()

dlThreads = [leftHandThread, savageThread, baboonThread]

#Wait for all threads to do their work.
for dlThread in dlThreads:
    dlThread.join()

print('Done for today!')