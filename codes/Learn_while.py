print("Hello welcome to the counsling Bot... Please tell me your name")
myname = input("Please enter your name")
print("Hello " +myname + " How are you ..!Is something wrong with you ")
feelingbad=True
while feelingbad:
    
    message = input("Why are are feeling bad ? May I know your problem ")
    message1 = "Is it feeling sorry for it , Please continue.."
    
    if message == 'quit':
        feelingbad=False
    else:
        print(message1)