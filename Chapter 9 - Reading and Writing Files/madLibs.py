#Mad Libs that reads text files and let user add their own words to replace certain words.

import pyinputplus as pyip 

madFile = open('madLibs.txt', 'w')
madFile.write('''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events. And we add a 3d NOUN to try the Discord conversation''')
madFile.close()
madFile = open('madLibs.txt')
words = madFile.read().split()

adjInput = pyip.inputStr(prompt = 'Enter an adjective ')
nounInput = pyip.inputStr(prompt = 'Enter a noun ')
verbInput = pyip.inputStr(prompt = 'Enter a verb ')
noun2Input = pyip.inputStr(prompt = 'Enter a 2nd noun ' )
noun3Input = pyip.inputStr(prompt = 'Enter a 3d noun ')
nounNum = 0

for i in range(len(words)):
    if words[i] == 'ADJECTIVE':
        del words[words.index('ADJECTIVE')]
        words.insert(i, adjInput)
    elif words[i] == 'NOUN' and nounNum == 0:
        del words[words.index('NOUN')]    
        words.insert(i, nounInput)
        nounNum += 1
    elif words[i] == 'VERB.':
        del words[words.index('VERB.')]
        words.insert(i, verbInput +'.')
    elif words[i] == 'NOUN' and nounNum == 1:
        del words[words.index('NOUN')]
        words.insert(i, noun2Input)
        nounNum += 1
    elif words[i] == 'NOUN' and nounNum == 2:
        del words[words.index('NOUN')]
        words.insert(i, noun3Input)

finalString = ' '.join(words)
madFile.close()
madFile = open('madLibs.txt', 'w')
madFile.write(finalString)
madFile.close()
print(finalString)