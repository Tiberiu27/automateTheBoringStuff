#! python3
#Deleting Uneeded Files

import os, sys

#move working directory to file's location
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

for folderName, subfolders, filenames in os.walk(dname):
    for filename in filenames:
        if os.path.getsize(os.path.join(folderName,filename)) > 100_000_000:
            print(os.path.abspath(filename) + ' this file is over 100mb!') 