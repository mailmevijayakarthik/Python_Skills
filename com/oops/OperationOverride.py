'''
Created on Nov 17, 2019

@author: vijayakarthikeyanarul
'''
class Students:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Students(m1,m2)
        print("Added...",s3.m1,s3.m2)
        return s3
    
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2) 
        
s1=Students(20,30)
s2=Students(50,80)

s3 = s1+s2  # Overloading add Operator 

# similarly we can do for > by implementing __gt__ 

print(s3) # overriding __str__ statement

name = "karthik"
print(name)
        