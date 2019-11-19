'''
Created on Oct 13, 2019

@author: vijayakarthikeyanarul
'''
a=10
class myLearning():
    
    def Hello(self):
        print("Happy Learning")

vk=myLearning
vk.Hello(a)

print(myLearning.__name__)
print(myLearning.__module__)
print(myLearning.__dict__)