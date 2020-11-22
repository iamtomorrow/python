#Classes and Objects Constructors with Input

class MyClass:
    def __init__(self, nameA, nameB, age, gender):
        self.first_name = nameA
        self.last_name = nameB
        self.actual_age = age
        self.your_gender = gender

a = str(input("1st name: "))
b = str(input("2nd name: "))
c = int(input("Age: "))
d = str(input("Gender: "))

userA = MyClass(a, b, c, d)

print(userA.first_name + userA.last_name)
