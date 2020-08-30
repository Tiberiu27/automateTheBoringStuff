#Date Detection
import re


while True:
    print('Enter a calendar date, something like dd/mm/yyyy')
    userDate = input()



    #Regular expression for dates dd/mm/yyyy or 0d/0m/yyyy

    dateRegex = re.compile(r'(^0?1?[0-9]|[0-2][1-9]|30|31)/(0?[1-9]|1[0-2])/([1-2][0-9][0-9][0-9])')
    mo = dateRegex.search(userDate)
    day, month, year = mo.groups()


    #Checking if the date is valid(considering leap years and 30 days month)
    def isValid():
        if month == '04' or month == '06' or month == '09' or month == '11':
            if int(day) in range(1, 31):
                return True
            else:
                return False
        elif (month == '02' and int(year) % 4 == 0) or (month == '02' and int(year) % 100 == 0) or (month == '02' and int(year) % 400 == 0):
            if int(day) in range(1, 30):
                return True
            else:
                return False
        elif month == '02':
            if int(day) in range(1, 29):
                return True
            else:
                return False
        else:
            if int(day) in range(1, 32):
                return True
            else:
                return False

    if isValid() == True:
        print('Congrats! your date (' + day + '/'+ month+ '/' + year + ') is valid!')
        break

    print('Thats not a valid date. try again')