#!python3
# spreadsheetToTextFiles.py - write contents of a spreadsheet into files.

import os, sys, openpyxl

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.active

for colNum in range(1, sheet.max_column + 1):
    texFile = open(str(colNum) + '.txt', 'w')
    for rowNum in range(1, sheet.max_row + 1):
        print(rowNum)
        texFile.write(str(sheet.cell(row = rowNum, column = colNum).value) + '\n')
    texFile.close()