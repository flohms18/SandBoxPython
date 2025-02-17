import random as rd 

class Car :
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model,
        self.year = year
    
    def GetCarBrand(self):
        return self.brand
    def SetCarBrand(self, x):
        self.Brand = x


Clio = Car("Renault","Clio",2004)
print(Clio.GetCarBrand())