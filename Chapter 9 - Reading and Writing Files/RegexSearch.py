#! Python3
#A program that opens all .txt files and searches for any line that maches
#a user supplied regular expression

from pathlib import Path
import re, os

#Search for lines in all text files and add them to a list
lines = []
p = Path('/RegexSearch')
for txtFile in p.glob('*.txt'):
    obj = open(txtFile)
    lines = lines + obj.readlines()
    obj.close()

#Create a regex that identifies the line with that the user wants and prints it
print('what do you wanna search for?')
regexInput = input()
regexPar = '.*' + regexInput + '.*'
printLines = []
for i in lines:
    colaRegex = re.compile(regexPar)
    if colaRegex.search(i) != None:
        printLines.append(colaRegex.findall(i))



print(printLines)