#Finally

'''try:
    print(x)
except:
    print("Something went wrong.")
finally:
    print("The 'try except' is finished")'''

try:
    f = open("demofile.txt")
    f.write("Lorum Ipsum")
except:
    print("Something went wrong when writing to the file.")
finally:
    f.close()
