#!python3
#autoUnsubscriber.py - A program that downloads all your emails and opens the unsubscribe page foe each one.

import webbrowser, bs4, pyzmail, imapclient

#Logging in the mail account.
emailLogin = input('Enter the email address: ')
passLogin = input('Enter the password: ')
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(emailLogin, passLogin)
#Selecting the INBOX folder and looping through messages.
imapObj.select_folder('INBOX', readonly= True)
UIDs = imapObj.search(['ALL'])
for i in UIDs:
    rawMessages = imapObj.fetch(i, ['BODY[]'])
    message = pyzmail.PyzMessage.factory(rawMessages[i][b'BODY[]'])
    messageLinks = message.html_part.get_payload().decode(message.html_part.charset)
    soup = bs4.BeautifulSoup(messageLinks, 'html.parser')
    try:
        unsubscribeLinkElem = soup.select("a[title='Dezabonare']")
        unsubscribeLink = unsubscribeLinkElem[0].get('href')
        webbrowser.open(unsubscribeLink)
    except:
        continue
imapObj.logout