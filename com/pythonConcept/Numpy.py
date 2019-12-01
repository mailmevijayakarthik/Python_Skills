from email.policy import linesep_splitter

from numpy import *

arr = array([5,3,4,2.0])

print(arr)
### Different ways of creating an Array
## Creating an Single dimension Array

arr1=linspace(1,40,5)
print(arr1)

arr2=arr
arr[3]=10
print("Original array : ",arr, id(arr))
print("Copy of array : ",arr2, id(arr2))

arr3=arr.view()
arr[3]=12
print("Original array : ",arr, id(arr))
print("Shallow Copy of array : ",arr3, id(arr3))

arr4=arr.copy()
arr[1]=100
print("Original array : ",arr, id(arr))
print("Deep Copy of array : ",arr4, id(arr4))