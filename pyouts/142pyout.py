#Object Methods

class Car:
    def __init__(self, Brand, Year):
        self.Brand = Brand
        self.Year = Year

    def myMethod(self):
        print("this car is  ", self.Brand)

userA = Car("Horse Power", 2026)
userA.myMethod()
