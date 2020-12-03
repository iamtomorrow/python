#Pyhton Lambda

def myFunctionA(x):
    return lambda y : y * x

myDobler = myFunctionA(2) 
print(myDobler(11))


def myFunctionB(x):
    return lambda y : y * x

myTripler = myFunctionB(3)
print(myTripler(5))
