# Delete Objects

class Users:
    def __init__(self, name, age):
        self.name = name
        self.age = age

userA = Users("John", 45)
userB = Users("Katharine", 34)
userC = Users("George", 24)

# deleting a object
del userB

print("name: ", userA.name, "age: ", userA.age)
#print("name: ", userB.name, "age: ", userB.age)
print("name: ", userC.name, "age: ", userC.age)
