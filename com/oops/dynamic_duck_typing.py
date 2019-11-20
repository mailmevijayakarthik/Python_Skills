'''
Created on Nov 17, 2019

@author: vijayakarthikeyanarul
'''
class PyCharm:
    def execute(self):
        print("Executing in PyCharm")
        print("Compiling in PyCharm")

class MyownEditor:
    def execute(self):
        print("Executing in PyCharm")
        print("Compiling in PyCharm")
        print("Debug my code in My custom editor")
        print("Reporting is modified")

class laptop:
    
    def code(self,ide):
        print("Tech laptop")
        ide.execute()
    
 
ide = PyCharm()   
custom = MyownEditor()     

lap1 = laptop()

lap1.code(custom)  # By changing the argument type of date from PyCharm to MyownEditor the code still works until the new class has its needed method in it 
                   # Called DUCK TYPING - doesn't actually matter what type my data is - just whether or not I can do what I want with it
