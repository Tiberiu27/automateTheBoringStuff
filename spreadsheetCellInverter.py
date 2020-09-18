#!python3
#spreadsheetCellInverter.py - inverts the columns and rows

import os, sys, openpyxl

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.active

cellValues = {}
#Saving values to a dictonary and deleting cells
for colNum in range(1, sheet.max_column + 1):
    for rowNum in range(1, sheet.max_row + 1):
        cellValues[colNum, rowNum] = sheet.cell(row = rowNum, column = colNum).value
        sheet.cell(row = rowNum, column = colNum).value = ''
#Writing values from dictionary to sheet
for k, v in cellValues.items():
    sheet.cell(row = k[0], column = k[1]).value = v

#Saving the file
wb.save('inverted' + str(sys.argv[1])[0].upper() + str(sys.argv[1])[1:])
print(cellValues)