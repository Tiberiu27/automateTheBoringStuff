#!python3
# pdfParanoia.py - a program that encrypts all pdf files ina folder and subfolders

import os, sys, PyPDF2,send2trash

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

#Finding all pdfs and ecrypting them with the password provided in the cmd line argument
for folderName, subfolders, filenames in os.walk(dname):
    for filename in filenames:
        if filename.endswith('.pdf'):
            filePath = os.path.join(os.path.abspath(folderName), filename)
            pdfReader = PyPDF2.PdfFileReader(filePath, 'rb')
            if not pdfReader.isEncrypted:
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pageObj = pdfReader.getPage(pageNum)
                    pdfWriter.addPage(pageObj)
                pdfWriter.encrypt(sys.argv[1])
                print('Encrypting...' + filePath)
                resultPdf = open (os.path.join(os.path.dirname(filePath), str(filename)[:-4] + "_encrypted.pdf"), 'wb')
                pdfWriter.write(resultPdf)
                resultPdf.close()

#Atempting to read encrypted files and read them, and delete the orignal, unencrypted
for folderName, subfolders, filenames in os.walk(dname):
    for filename in filenames:
        if filename.endswith('_encrypted.pdf'):
            filePath = os.path.join(os.path.abspath(folderName), filename)
            pdfReader = PyPDF2.PdfFileReader(filePath, 'rb')
            if pdfReader.isEncrypted:
                succesfulDecrypt = pdfReader.decrypt(sys.argv[1])
                if succesfulDecrypt:
                     print('succesful read from: ' + os.path.abspath(filePath))
        #Deleting files that are not encrypted
        elif filename.endswith('.pdf'):
            filePath = os.path.join(os.path.abspath(folderName), filename)
            pdfReader = PyPDF2.PdfFileReader(filePath, 'rb')
            if not pdfReader.isEncrypted:
                print("Deleting... " + filePath)
                send2trash.send2trash(filePath)