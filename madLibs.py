#Mad Libs that reads text files and let user add their own words to replace certain words.

from pathlib import Path 
import pyinputplus as pyip 

madFile = open('madLibs.txt', 'w')
madFile.write('''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events''')
madFile.close()
madFile = open('madLibs.txt')
words = madFile.read().split()

adjInput = pyip.inputStr(prompt = 'Enter an adjective ')
nounInput = pyip.inputStr(prompt = 'Enter a noun ')
verbInput = pyip.inputStr(prompt = 'Enter a verb ')
noun2Input = pyip.inputStr(prompt = 'Enter a 2nd noun ' )
secondNoun = False

for i in range(len(words)):
    if words[i] == 'ADJECTIVE':
        del words[words.index('ADJECTIVE')]
        words.insert(i, adjInput)
    elif words[i] == 'NOUN' and secondNoun == False:
        del words[words.index('NOUN')]
        words.insert(i, nounInput)
        secondNoun = True
    elif words[i] == 'VERB.':
        del words[words.index('VERB.')]
        words.insert(i, verbInput +'.')
    elif words[i] == 'NOUN' and secondNoun == True:
        del words[words.index('NOUN')]
        words.insert(i, noun2Input)


finalString = ' '.join(words)
madFile.close()
madFile = open('madLibs.txt', 'w')
madFile.write(finalString)
madFile.close()
print(finalString)