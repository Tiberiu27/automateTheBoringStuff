#!python3
#commandLineEmailer.py - takes from command line an email address and some text
# logs in the mail client and sends a mail
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys,time

if len(sys.argv) > 1:
    emailAdress = sys.argv[1]
    emailText = sys.argv[2:]
    browser = webdriver.Firefox()
    browser.get('https://gmail.com')
    userElem = browser.find_element_by_id('identifierId')
    time.sleep(2)
    userElem.send_keys('EMAILADRESS')
    userElem.send_keys(Keys.ENTER)
    time.sleep(2)
    passElem = browser.find_element_by_css_selector('.I0VJ4d > div:nth-child(1) > input:nth-child(1)')
    passElem.send_keys('YOURPASSWORD')
    passElem.send_keys(Keys.ENTER)
    time.sleep(5)
    writeButton = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
    writeButton.click()
    time.sleep(5)
    destEmail = browser.find_element_by_name('to')
    destEmail.send_keys(emailAdress)
    subjBox = browser.find_element_by_name('subjectbox')
    subjBox.send_keys('test')
    bodyEmail = browser.find_element_by_xpath('//*[@role="textbox"]')
    bodyEmail.send_keys(emailText)
    sendButton = browser.find_element_by_xpath('//*[@aria-label="Trimite ‪(⌘Enter)‬"]')
    sendButton.click()