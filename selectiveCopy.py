#! python3
#selectiveCopy.py - copy certain files with a certain extension to another location.
import shutil, os, sys

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

if not os.path.exists('PhotosContainer'):
    os.mkdir('PhotosContainer')
   
fileDestination = os.path.join(dname, 'photosContainer')
for foldername, subfolders, filenames in os.walk(dname):
    for filename in filenames:
        if filename.endswith('.png'):
            print(f'copying file {os.path.join(foldername, filename)} to {fileDestination}')
            try:
                shutil.copy(os.path.join(foldername, filename), fileDestination) 
            except shutil.SameFileError:
                pass


