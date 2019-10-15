'''
Created on Oct 13, 2019

@author: vijayakarthikeyanarul
'''

class Attributes_learning():
    def __init__(self):
        self.__private=("I am private")
        self._myprotected=("I am protected")
        self.allpublic=("I am public")
        

    def __privatemethod(self):
        print("Inside the Private method")    
        
obj=Attributes_learning()
obj._Attributes_learning__privatemethod()
print(obj._Attributes_learning__private)
print(obj.allpublic)
print(obj._myprotected)
