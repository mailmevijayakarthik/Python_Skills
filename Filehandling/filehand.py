with open("fruits.txt","r") as source:
    content=source.read()
    print(content)
with open("fruits.txt","a+") as rework:
    rework.write("\nmango")
    rework.seek(0)
    newcontent=rework.read()
    print("After rework:")
    print(newcontent)

with open("fruits.txt","a+") as myfile:
    mycontent=myfile.read()
    myfile.write(mycontent)
    myfile.write(mycontent)
    myfile.seek(0)
    print(myfile.read())
