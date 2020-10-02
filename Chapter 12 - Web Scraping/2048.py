#!python3
#2048.py - opens https://gabrielecirulli.github.io/2048/ and plays the game automatically

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


webbrowser = webdriver.Firefox()
webbrowser.get('https://gabrielecirulli.github.io/2048/')
time.sleep(5)
htmlElem = webbrowser.find_element_by_tag_name('html')
gameStatusElem = webbrowser.find_element_by_class_name('game-container')
while 'Game over!' not in gameStatusElem.text:
    htmlElem.send_keys(Keys.UP)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.LEFT)
    gameStatusElem = webbrowser.find_element_by_class_name('container')


if 'Game over!' in gameStatusElem.text:
    print('bye!')
    time.sleep(3)
    webbrowser.close()