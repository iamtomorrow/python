#Classes and Objects
import datetime

outYear = datetime.datetime.today()

class Register:
    def __init__(self, Name, Birth, Age):
        self.aName = Name
        self.aBirth = Birth
        self.aAge = Age

userA = Register("Onell", 2000, 0)
userAAge = outYear.year - userA.aBirth

userB = Register("Carl", 1996, 0)
userBAge = outYear.year - userB.aBirth

print("User A:")
print("Name: ", userA.aName, "\nBirth: ", userA.aBirth, "\nAge: ", userAAge, "years")

print("\nUser B:")
print("Name: ", userB.aName, "\nBirth: ", userB.aBirth, "\nAge: ", userBAge, "years")
