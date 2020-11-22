#Creating another class

class Vehicle:
    def __init__(self, brand, model, year):
        self.aBrand = brand
        self.aModel = model
        self.aYear = year

carA = Vehicle("Horse Power", "HPX", 2026)
carB = Vehicle("Horse Power", "Pa V12", 2029)

print("Brand: ", carA.aBrand, "\nModel: ", carA.aModel, "\nYear: ", carA.aYear)
print("")
print("Brand: ", carB.aBrand, "\nModel: ", carB.aModel, "\nYear: ", carB.aYear)
