#!Python3
#pdfDeparanoia.py - find all encrypted PDFs and create a unencrypted copy of them.

import os, sys, PyPDF2

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

for folderName, subfolders, filenames in os.walk(dname):
    for filename in filenames:
        if filename.endswith('.pdf'):
            filePath = os.path.join(os.path.abspath(folderName), filename)
            pdfReader = PyPDF2.PdfFileReader(filePath, 'rb')
            if pdfReader.isEncrypted:
                succesfulDecrypt = pdfReader.decrypt(sys.argv[1])
                if succesfulDecrypt:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pageObj = pdfReader.getPage(pageNum)
                        pdfWriter.addPage(pageObj)
                    pdfResult = open(filePath[:-4] + '_decrypted.pdf','wb')
                    pdfWriter.write(pdfResult)
                    pdfResult.close()
                else:
                    print('wrong password, mate.')