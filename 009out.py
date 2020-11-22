#Method Objects

# creating my class
class Users:
    # creating the __init__() function with parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # creating my function called myMethod
    def myMethod(self):
        print(f"my name is {self.name}, I am {self.age} years.")

# creating my objects
UserA = Users("Elon", 34)
UserB = Users("Carl", 87)

# calling my methd
UserA.myMethod()
UserB.myMethod()
