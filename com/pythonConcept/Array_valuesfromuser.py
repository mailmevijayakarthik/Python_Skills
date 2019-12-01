from array import *

arr = array('i',[])

n = int(input("Enter the total length of the array "))

for i in range(n):
    x= int(input("Enter the next value "))
    arr.append(x)

print(arr)

def search(x):
    found = False
    c=0
    for i in arr:
        c+=1
        if i==x:
            print("Found ",c)
            found=True
            break
    return found

x=search(int(input("Enter the number to search in the array ")))

if x is True:
    print("Element is found ")
else :
    print("Element not found")