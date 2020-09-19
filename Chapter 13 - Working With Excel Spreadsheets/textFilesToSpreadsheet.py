#!python3
# textFilesToSpreadsheet.py - write text files to a spreadsheet

import sys, os, openpyxl, glob

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

wb = openpyxl.Workbook()
sheet = wb.active

for colIndex, textFile in enumerate(sorted(glob.glob('*.txt')), 1):
    f = open(textFile)
    for rowIndex, i in enumerate(f.readlines(), 1):
        sheet.cell(row = rowIndex, column = colIndex).value = i
   
    f.close()

wb.save('textToSheet.xlsx')