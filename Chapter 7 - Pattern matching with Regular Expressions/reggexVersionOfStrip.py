import re

# A function that takes a string and does the same thing as the strip() string method
# if no other arguments are passed strip the whitespace from start and end of string
#if arguments are passed strip the arguments from start and end. Simple right?

def stripper():
    print('Enter the text you wanna strip *wink*')
    txt = input('')

    print('''If you want to strip something else then whitespace please specify,
    otherwise leave blank''')
    argum = input('')
    if argum == '':
        txtReggex = re.compile(r'^(\s+)|(\s+$)')
        mo = txtReggex.sub('',txt)
        print(mo)
        print(len(mo))
    else:
        argumReggex = re.compile(argum)
        mo2 = argumReggex.sub('',txt)
        print(mo2)
        print(len(mo2))


stripper()