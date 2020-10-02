#!python3
#flickrDownloader.py

import os, requests, bs4,webbrowser, re, threading


os.makedirs('flickr', exist_ok=True)
url = 'https://www.flickr.com/search/?text='
usrInput = input('What you wanna search? ')
url = url + str(usrInput) #Only for test
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
photoElem = soup.select('.photo-list-photo-view')
def download_image(url):
    with open(os.path.join('flickr', os.path.basename(url)), 'wb') as f:
        f.write(requests.get(url).content)
    print(url, 'download successufly')

for elem in photoElem:
    img_url = 'https:' + re.search(r'url\((.*)\)', elem.get("style")).group(1)
    threading.Thread(target=download_image, args=(img_url,)).start()

    


