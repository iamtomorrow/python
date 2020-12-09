#The strftime() Method

import datetime

x = datetime.datetime.now()

print(x.strftime("%a")) # Weekday, short version
print(x.strftime("%A")) # Weekday, full version
print(x.strftime("%w")) # Weekday as a number 0-6, 0 is Sunday
print(x.strftime("%d")) # Day of month 01-31
print(x.strftime("%B")) # %B Month name, full version
print(x.strftime("%b")) # %b Month name, short version
