#!python3
#excelToCsv.py
import os, openpyxl, csv, sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

for excelFile in os.listdir('.'):
    #Skip non-xlsx files, load the workbook obj
    if not excelFile.endswith('.xlsx'):
        continue
    wb = openpyxl.load_workbook(excelFile)
    for sheetName in wb.sheetnames:
        #Loop through every sheet in the workbook.
        sheet = wb[sheetName]
    
        #Create the CSV filename from the excel filename and sheet title.
        csvFileName = excelFile.split('.')[0]+ '_' + sheet.title + '.csv'
        csvFile = open(csvFileName, 'w', newline='')
        #Create the csv.writer obj for this CSV file.
        csvWriter = csv.writer(csvFile)

        #Loop through every row in the sheet.
        for rowNum in range(1, sheet.max_row + 1):
            rowData = [] #append each cell to this list
            #Loop throufg each cell in the row
            for colNum in range(1, sheet.max_column + 1):
                #Append each cell's data to rowData.
                rowData.append(sheet.cell(row = rowNum, column = colNum).value)
                

            
            #Write the rowData list to the CSV file.
            csvWriter.writerow(rowData)

        csvFile.close()