#python3
#randomChore.py - takes a random person from a list and emails him to do a chore 
import os, sys, openpyxl, smtplib, random

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

#Login into email account*.
#*Using a gmail account with lesssecureapps option enabled.
emailLogin = input('What\'s your email? ')
passLogin = input('What\'s your secret password? ')
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(emailLogin, passLogin)

#Loading the Excel workbook and sheet
wb = openpyxl.load_workbook('randomChores.xlsx')
sheet = wb.active

people = {}
chores = []
for i in range (2, sheet.max_row + 1):
    name = sheet.cell(row= i, column= 1).value
    email = sheet.cell(row= i, column= 2).value
    chore = sheet.cell(row= i, column= 3).value
    people[name] = email
    chores.append(chore)

#Assigning a unique random chore to a random individual.
listName = list(people.keys())
for k, v in people.items():
    #Next four lines ensure that is a unique random task.
    randomChore = random.choice(chores)
    chores.remove(randomChore)
    randomIndividual = random.choice(listName)
    listName.remove(randomIndividual)

    body = 'Subject: %s task for today.\nDear %s,\nToday you\'re assigned with this special task. Enjoy!' %(randomChore, randomIndividual)
    print('Sending email to...%s' % randomIndividual)
    smtpStatus = smtpObj.sendmail(emailLogin, people[randomIndividual], body)
    if smtpStatus != {}:
        print('There was a problem sending email to %s at %s'% (randomIndividual, people[randomIndividual]))

smtpObj.quit()