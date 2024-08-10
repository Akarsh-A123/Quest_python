""" Write a program to move a file in directory 'source' and copy it to 'destination'. Handle necessary exceptions:
. if file does not exists in source, print "no file found in source".
. if same file already exists in target, print "file with same name already exists"""

import shutil
try:
    source = 'source/file1.txt'
    destination = 'destination/file1.txt'
    shutil.copyfile(source,destination)
except FileNotFoundError:
    print('File is not fount')
except:
    print('File already exist')