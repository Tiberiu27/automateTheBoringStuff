#! python3
#linkVerification.py - a program that download every URL on a given webPage and flag pages that have a 404 error
import requests, bs4, re

url = input('Hit me with that URL! ')
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
linkElem = soup.select('a')
for element in linkElem:
    childUrl = element.get('href')
    try:
        if childUrl.startswith('http'):
            try:
                res = requests.get(childUrl)
                res.raise_for_status()
                print(childUrl)
            except:
                if res.status_code == 404:
                    print('Broken link')
                continue
    except:
        continue