import re

print(''''Please enter a strong password (at least 1 uppercase, 1 lowercase and a digit)
Remember, your password is safe with us and we won't share or sell your data *wink*''')

while True:
    password = input()


    def passCheck():
        passRegex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}')
        mo = passRegex.search(password)
        if mo != None:
            return True

    if passCheck() == True:
        print('Thats a strong password indeed!')
        break
    else:
         print('Oops! Not a good one. Try again.')


    passCheck()