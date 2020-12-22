#Global Keyword

'''def myFunc():
    global y
    y = 20
    print(y)

myFunc()
print(y)'''

y = 70

def myFunc():
    global y
    y = 40
    print(y)

myFunc()
print(y)
