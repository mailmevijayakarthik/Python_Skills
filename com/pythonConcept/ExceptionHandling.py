class LearnException:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def division(self):
        try:
            div=self.a/self.b
            print(div)
        except Exception as e:
            print("Invalid entry",e)
        
        

L1=LearnException(5,0)
L1.division()
        