#Change Tuple Values

x = ("apple", "banana", "kiwi")
y = list(x)
y[0] = "strawberry"
x = tuple(y)

print(x)
