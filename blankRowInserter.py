#!python3
#blankRowInserter.py - a program that takes 2 integers and a filename and inserts blank rows

import os, sys, openpyxl

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

if len(sys.argv) < 5:
    srcBook = openpyxl.load_workbook(sys.argv[3])
    sheet = srcBook.active
    for i in range(int(sys.argv[2])):
        sheet.insert_rows(int(sys.argv[1]))


    srcBook.save('blankRowed ' + sys.argv[3])
else:
    print('too many arguments!')