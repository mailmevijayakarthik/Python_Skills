mystudentdict={"Karthik":"Expert","Vijay":"Lead","Stalin":"Memeber"}

for stud in mystudentdict.items():
    print("{} is my student who is an {}".format(stud[0],stud[1]))

for stud in mystudentdict.keys():
    print("{} is my student ".format(stud))

for stud in mystudentdict.values():
    print("My student is a {} ".format(stud))


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for contacts in phone_numbers.values():
    print(contacts.replace("+","00"))