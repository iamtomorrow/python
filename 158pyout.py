#Function Inside Function

def myFunc():
    y = 8
    def myInnerFunc():
        print(y)
    myInnerFunc()

myFunc()
