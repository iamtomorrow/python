#Default Value Parameter

def MyCountries(country = "Sweden"):
    print("country: " + country)

MyCountries("USA")
MyCountries()                       #The value that will appear here is the default parameter, "Sweden"
MyCountries("Canada")
MyCountries("Denmark")
