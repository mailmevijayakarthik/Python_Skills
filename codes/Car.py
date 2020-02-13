class car():

    def __init__(self, name, model):
        self.name=name
        self.model=model
    

    def carType(self):
        print(self.name + "is an Luxary car ")
    
    def carresellvalue(self):
        print(self.name + self.model + "Have a very less resell value")

mycar=car('mazda',' Mazda 3')
mycar.carType()
mycar.carresellvalue()