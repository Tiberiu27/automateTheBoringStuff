#!python3
# bruteForcePDF.py - trying passwords from a dictionary to decrypt a PDF file.

import os, sys, PyPDF2

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

usrInput = input('what file you wanna crack?')

passDict = open('dictionary.txt')
passDictList = passDict.read().split('\n')
filePath = os.path.abspath(usrInput)
pdfFile = open(filePath, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
if pdfReader.isEncrypted:
    for password in passDictList:
        print('Trying password... ' + password)
        if pdfReader.decrypt(password) == 1:
            print('Yey! Decryption succesful, password was ' + password)
            break
        elif pdfReader.decrypt(password.lower()) == 1:
            print('Yey! Decryption succesful, password was ' + password.lower())
            break

else:
    print('The file is not encrypted, dummy')