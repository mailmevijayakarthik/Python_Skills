'''
Created on Oct 13, 2019

@author: vijayakarthikeyanarul
'''
class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def getArea(self):
        print("Area of the Rectangle is :", self.length*self.breadth)
        

class Square(Rectangle):
    def __init__(self,side):
        self.side=side
        Rectangle.__init__(self, side, side)
        
    def getArea(self):
        print("Area of the Square is :", self.side*self.side)
        

r=Rectangle(2,5)
s=Square(10)
r.getArea()
s.getArea()

        