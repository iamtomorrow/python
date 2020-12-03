#Python Arrays

#Example
cars = ["Volvo", "Ford", "Tesla"]

#Access the elements of an Array
print(cars[2])

#Modify the value of a element inside a Array
cars[0] = "Horse Power"

#The Length of a Array
print(len(cars))

#Loping Array elements
for c in cars:
    print(c)

#Adding Array Elements
cars.append("Lamborghini")
cars.insert(0, "Toyota")

#Removing Array Elements
#del cars[3]
#cars.pop(2)
cars.remove("Horse Power")

print(cars)
