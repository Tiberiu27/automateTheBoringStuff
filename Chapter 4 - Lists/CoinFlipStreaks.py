import random

numberOfStreaks = 0

for experimentNumber in range(1000):
    #Code that creates a list of 100 'heads' or 'tails' values.
    coinList = []
    while len(coinList) < 100:
        for i in range(random.randint(0,2)):
            if i == 0:
                coinList.append('T')
            elif i == 1:
                coinList.append('H')


    #Code that checks if there is a streak of 6 heads or tails in a row.

    for j in range(0, len(coinList) -5):
          if coinList[j] == coinList[j +1] == coinList[j +2] == coinList[j +3] == coinList[j +4] == coinList[j +5]:
              numberOfStreaks += 1


print(coinList) #testing the ingerity of the list
print(len(coinList)) #Checking the length of the list
print(numberOfStreaks)#Bullshit
print('Chance of streak: %s%%' %(numberOfStreaks / 100))