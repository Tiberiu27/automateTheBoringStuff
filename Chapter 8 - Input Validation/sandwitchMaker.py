import pyinputplus as pyip 

print('''Welcome to the Sandwitch Maker, my name is Kendrick and 
I'll make the sandwitch for you. Let's see...''')
breadPrompt = 'What kind of bread would you like?\n'
breadType = pyip.inputMenu(['wheat','white','sourdough'], numbered= True, prompt = breadPrompt)
proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered= True, prompt = 'Meat?\n')
cheeseTopping = pyip.inputYesNo(prompt = 'Want cheese?\n')
sandwitchCount = pyip.inputInt(prompt = 'How many of them do you want?\n', min=1)

total = 0

if breadType == 'wheat':
    total += 3
elif breadType == 'white':
    total += 2
else:  #What's a sourdought btw!?
    total = 6 

if proteinType == 'chicken':
    total += 2
elif proteinType == 'turkey':
    total += 4
elif proteinType == 'ham':
    total += 2
else:
    total += 5

if cheeseTopping == 'yes':
    total += 3


print('Ok, that will be: ' + str(total * sandwitchCount) + ' MDL')