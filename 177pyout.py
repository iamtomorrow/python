#Convert from Python to JSON

import json

# a Python object (dict)
x = {"name": "Johnson", "age": 56, "city": "Chicago"}

# convert into JSON
y = json.dumps(x)

# the result is a JSON string
print(y)
