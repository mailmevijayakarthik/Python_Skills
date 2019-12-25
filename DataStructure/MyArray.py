MyArray=[5,10,6,20,29]

print(MyArray[2])
MyArray[1]="Karthik"
print(MyArray)
print(MyArray[:-1])

MyNumber=[5,100,6,20,29]

max=MyNumber[0]
for i in MyNumber:
    if i>max:
        max=i

print(max)