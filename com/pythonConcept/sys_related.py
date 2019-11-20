'''
Created on Oct 12, 2019

@author: vijayakarthikeyanarul
'''
import sys
import os

# print(sys.argv)
# 
# print(len(sys.argv))
# 
# str = input("Enter the 4 digit number")
# print("Entered number ", str)

# Open the file in write mode 
newfile=open("Testing.txt", "w+")
newfile.seek(1000)
print (newfile.name)

# for i in range (10):
#     newfile.write("I am karthikeyan \n")
#     print(newfile.read())
#      
#      
#      
    


#newfile.close()


#Rename the file's name 
#os.renames("myTestDatafile.txt", "Testing.txt")