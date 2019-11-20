
#with open('source.loc.txt', 'r') as myfile:
   # myfile_content=myfile.read()
   # print(myfile_content)

#---------------------------------------------------------------
    # To Reads one line at a time 
    #f_content=myfile.readline()
    
    #print(f_content)
    
   #--------------------------------------------------------------- 
  #  Prints all the lines one by one 
#    for line in myfile:
#        print(line,end='')


################################### To Write a file 

#with open('NewDestination.txt','a') as W:
#    W.write("\nI am vijay")

################################### Create folder and working with directories 

import os

def directorydetails():
    print(os.getcwd())

def changedirectory():
    print(os.getcwd())
    os.chdir('C:/Users/242074/git/HEB.COM/src/main/resources/common/locators')
    print(os.getcwd())
    
def createnewfolder():
    os.mkdir('New_Test')

def deletefolder():
    os.rmdir('New_Test')
    
def listoffilesandfolder():
    print(os.listdir())
    
def renamethefolder():
    os.renames('NewDestination.txt', 'UpdatedDestination.txt')

def revertrenamethefolder():
    os.renames('UpdatedDestination.txt', 'NewDestination.txt')

    
directorydetails()
#changedirectory()
createnewfolder()
deletefolder()
listoffilesandfolder()
renamethefolder()
revertrenamethefolder()
