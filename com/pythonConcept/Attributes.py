'''
Created on Oct 13, 2019

@author: vijayakarthikeyanarul
'''

class Attributes_learning():
    def __init__(self):
        self.__private=("I am private variable")
        self._myprotected=("I am protected variable ")
        self.allpublic=("I am public variable")
        

    def __privatemethod(self):
        print("\nInside the Private method")    
        
obj=Attributes_learning()
obj._Attributes_learning__privatemethod()
print(obj._Attributes_learning__private)
print(obj.Attributes_learning.allpublic)
#print(obj.allpublic)
#print(obj._myprotected)
