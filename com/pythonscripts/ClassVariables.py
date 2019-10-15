'''
Created on Oct 13, 2019

@author: vijayakarthikeyanarul
'''
class Learningvariables():
    Master="Dandayathapani"       # class variable
    def setSubject(self,subject):
        self.subject=subject


obj1=Learningvariables()       #instance variable
obj2=Learningvariables()
obj1.Master="Aadhi"   # class variable is shared btw instances obj1 and obj2 
print(obj1.Master)
print(obj2.Master)


obj1.setSubject("Python")
obj2.setSubject("ML")

print(obj1.subject)    #instance variable
print(obj2.subject)     #instance variable