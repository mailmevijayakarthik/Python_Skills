def getallinputs(member):
    print("Below is the detail of",member)
    firstname=member
    lastName="Arul"
    age=31
    country="India"
    print("FirstName :", firstname,"LastName :", lastName ,"Age :", age, "Country :", country)
    getaddress(member)
    getfamilydetails(member)
    boringFunction()

def getaddress(Person):
    presentAddress=Person+"'s Address is "+"4114 Medical Dr Apt 1202, San Antonio"
    permanentAddress="Chennai,TamilNadu"

def getfamilydetails(member):
    print("Below is the detail of",member)
    kids=1
    members=4
    Adults=3

def boringFunction():
    print("'Boredom Mode' ON.")
    return 123


person=getallinputs("Vijay")
person=getallinputs("Karthik")
count = boringFunction()
print(count)
   

