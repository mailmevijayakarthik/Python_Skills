import os
from test.test_unicode_file_functions import filenames


def writeUniquerecords(dirpath,filenames):
    sourcepath=os.path.join(dirpath,filenames)
    with open(sourcepath,'r') as fp:
        lines= fp.readlines()
        destination_lines=[]
        for line in lines:
            if line not in destination_lines:
                destination_lines.append(line)
    
    destinationfile='/Users/vijayakarthikeyanarul/git/python_Skills/com/filehandling/UpdatedFolder'
    destipath=os.path.join(destinationfile,filenames)
    with open(destipath, "w+")as destination:
        destination.write("\n".join(destination_lines))            


def Readandwrite():
    for dirpath,dirnames,filenames in os.walk('/Users/vijayakarthikeyanarul/git/python_Skills/com/filehandling/locators'):
        print('Current Path',dirpath)
        print('Current Folder names',dirnames)
        print('Current Files names ',filenames)
        for file in filenames:
            writeUniquerecords(dirpath,file)
        
    

Readandwrite()