#!python3
#Filling in the gaps, if you have a file sequance x1.txt, x2.txt x4.txt renames them so you have a seq without gaps

import sys, shutil, os
from pathlib import Path

#move working directory to file's location
abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

p = Path(Path.cwd() / 'spammy')
fileList = list(p.glob('*0??.txt'))
fileList.sort()
i = 0
for textFileObj in fileList: #Loop through files that ends with numbers
    i = i + 1
    textFile = os.path.basename(textFileObj) #convert Path obj to str
    textFileAsList = list(textFile)
    textFileAsList[-5] = str(i)
    textFileAsList = ''.join(textFileAsList)
    dst = os.path.dirname(textFileObj)
    print('renaming ' + str(textFileObj) + ' to ' + os.path.join(dst, textFileAsList))
    shutil.move(textFileObj,os.path.join(dst, textFileAsList) )
    
    
        
    