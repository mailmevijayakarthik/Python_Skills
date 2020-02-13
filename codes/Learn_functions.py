def Welcome_Message(EmpName):
    for mylist in EmpList:
        print("Welcome to the club "+ mylist + " Have a nice day ahead")

    
EmpList=['Karthik','avk','vijaykarthik','Arul']
Welcome_Message(EmpList)

######################################################## Modifing a List 
#And Reverse its position


def updateJobs(uncompletedJob,completedJob):
    while uncompletedJob:
        currentJob=uncompletedJob.pop()
        completedJob.append(currentJob)
    
    
def printmyList():
    print(uncompletedJob)
    print(completedJob)
uncompletedJob=['Job_1','Job_2','Job_3','Job_4']
completedJob=[]
#updateJobs(uncompletedJob,completedJob)
# To print the original list from modification we can pass a copy of the existing list as below 
updateJobs(uncompletedJob[:],completedJob)
printmyList()