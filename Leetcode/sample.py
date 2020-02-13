def welcome(s):
    message = s
    output="Hello, World.\n"+message
    print(output)
    return output

def reverselist(mylist):
    res=[]
    n=len(mylist)
    for i in range(n-1,-1,-1):
        res.append(mylist[i])
    return res

#welcome("Welcome to 30 Days of Code!")
mylist=[2,4,6,8]
print(reverselist(mylist))