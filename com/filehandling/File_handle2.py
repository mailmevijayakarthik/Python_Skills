import os

filepath='C:/Users/242074/git/Python_Skills/com/filehandling/locators'
destinationpath='C:/Users/242074/git/Python_Skills/com/filehandling/UpdatedFolder'
filename='storeloc_updated.loc.txt'
newpath=os.path.join(destinationpath,filename)
#newpath='C:/Users/242074/git/Python_Skills/com/filehandling/UpdatedFolder/storeloc_updated.loc.txt'
print(newpath)
with open(newpath,'w') as f:
    pass
