    
import os

basepath = 'C:/Users/242074/git/HEB.COM/src/main/resources/common/locators'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():
            print(entry.name)
        if entry.is_dir():
            pass
            
            



#for entry in os.scandir(basepath):
#    if os.path.isfile(os.path.join(basepath, entry)):
#        print(entry)
   
            