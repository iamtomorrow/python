#Classes and Objects

class Vehicle:
    def __init__(self, brand, model, year):
        self.aBrand = brand
        self.aModel = model
        self.aYear = year

carA = Vehicle("Tesla", "ModelX", 2020)
carB = Vehicle("Horse Power", "HPX", 2026)
carC = Vehicle("Lamborghini", "Huracan", 2015)
carD = Vehicle("Porsche", "Porsche 911", 1964)

print("Vehicle A")
print("Brand: ", carA.aBrand, "\nModel: ", carA.aModel, "\nYear: ", carA.aYear)
print("\nVehicle B")
print("Brand: ", carB.aBrand, "\nModel: ", carB.aModel, "\nYear: ", carB.aYear)
print("\nVehicle C")
print("Brand: ", carC.aBrand, "\nModel: ", carC.aModel, "\nYear: ", carC.aYear)
print("\nVehicle D")
print("Brand: ", carD.aBrand, "\nModel: ", carD.aModel, "\nYear: ", carD.aYear)
