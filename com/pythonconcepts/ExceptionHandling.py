'''
Created on Nov 17, 2019

@author: vijayakarthikeyanarul
'''

class LearnExceptionHandling:
    
    
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def div(self):
        try:
            div=self.a/self.b
           
            print(div)
        
        except ZeroDivisionError as e:
            print("Wrong Input values ",e)
        except ValueError as e:
            print("Invalid input",e)    
        except Exception as e:
            print("Something went wrong",e)
        finally:
            print("Thanks for Dividing ")    
             
E=LearnExceptionHandling(5,0)
E1=LearnExceptionHandling(5,"p")
#E.div()
E1.div()