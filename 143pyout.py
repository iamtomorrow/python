#The self parameter

class myClass:
    def __init__(mysilliobject, name, year):
        mysilliobject.name = name
        mysilliobject.year = year

    def myMethod(abc):
        print("your name is ", abc.name) 

userB = myClass("Jonhson", 56)
userB.myMethod
