#Parse JSON - Convert from JSON to Python

import json

# a JSON object (dict)
x = '{"name": "George", "age": 34, "city": "Los Angeles"}'

# convert into Python 
y = json.loads(x)

# the result is a Python dictionary
print(y["name"])
