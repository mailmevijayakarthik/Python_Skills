class Birds:
    def __init__(self,name,color,size):
        self.name=name
        self.color=color
        self.size=size
    
    def birddetails(self):
        print("The Bird name is %s and Its Colour is %s which is of Size %s" %(self.name,self.color,self.size))
       


    def birdnature(self):
        if(self.size=="Medium"):
            print("All Medium birds are in ZOO")
            self.dance="Will dance"
        elif(self.size=="Large"):
            print("All Large birds are in Ocean/Forest")
            self.dance="Will Not dance"


            
Bird1=Birds("Pecock","Green","Medium")
Bird2=Birds("Penguin","Black&White","Large")

Bird2.birdnature()
Bird2.birddetails()
print(Bird2.dance)
   