def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

def startfromzeroto(n):
    mylist=[]
    for i in range(0,n):
        mylist.append(i)
    return mylist
#print(strangeListFunction(50))
x=int(input("Enter the number :"))
print(startfromzeroto(x))
