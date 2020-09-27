#!python3
#umbrellaReminder.py - reminds me every rainy morning to take your umbrella 
import sys, os, requests, bs4, re

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

url = 'https://www.vremea.ro/cluj/clujnapoca/'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
weatherStatusElem = soup.select('.txtnow')
#Selecting the text responsible for describing weather condition
mo = re.findall('<p class="txtnow">(.*)<br', str(weatherStatusElem[0].getText))
weatherStatus = mo[0]
weatherStatus.replace(' ', '') #Removing any white spaces
if weatherStatus == 'ploi' or weatherStatus == 'ploaie':
    print('Get your umbrella')

   