#Classes and Objects

class Rocket:
    def __init__(self, aName, aMass, aHeigh, aDiameter, aThrust, aEngine, aBooster):
        self.Name = aName
        self.Mass = aMass
        self.Heigh = aHeigh
        self.Diameter = aDiameter
        self.Thrust = aThrust
        self.Engine = aEngine
        self.Booster = aBooster

Falcon = Rocket("Falcon", 549.040, 70, 3.7, 1.7e6, "Merlin", False)

print("Name: ", Falcon.Name)
print("Mass: ", Falcon.Mass, "kg")
print("Heigh: ", Falcon.Heigh, "m")
print("Diameter: ", Falcon.Diameter, "m")
print("thrust: ", Falcon.Thrust, "lbs")
print("Engine: ", Falcon.Engine)
print("Booster: ", Falcon.Booster)
