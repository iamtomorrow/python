#Format the Result

import json

x = {
    "name": "George", 
    "age": 65,
    "married": True,
    "cars": [
        {"model": "Tesla ModelX", "mph": 200},
        {"model": "Horse Power", "mph": 300}
    ]}

y = json.dumps(x, indent=2, separators=(". ", " = "))
print(y)
