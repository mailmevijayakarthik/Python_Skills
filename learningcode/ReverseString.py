class ReverseMyString:
    def __init__(self,name):
        self.name=name
    
    def reverseme(self):
        print("Original String is "+ self.name)
        print("Reversed String is "+ self.name[::-1])

str1=ReverseMyString("Vijayakarthikeyan")
str1.reverseme()
