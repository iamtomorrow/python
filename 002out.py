#Classes and Objects Constructors

class MyClass:
    def __init__(self, nameA, nameB, age):
        self.your_first_name = nameA
        self.your_last_name = nameB
        self.your_age = age

userA = MyClass("George", "Onell", 29)
userB = MyClass("Catherine", "Reyes", 27)
userC = MyClass("Timot", "Reyes", 5)
userD = MyClass("Gyna", "Rodrigues", 2)

print(userA.your_first_name, userA.your_last_name, ", ", userA.your_age, "years old")
print(userB.your_first_name, userB.your_last_name, ", ", userB.your_age, "years old")
print(userC.your_first_name, userC.your_last_name, ", ", userC.your_age, "years old")
print(userD.your_first_name, userD.your_last_name, ", ", userD.your_age, "years old")
