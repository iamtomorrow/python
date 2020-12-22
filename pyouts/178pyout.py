#Converting Python objects into JSON strings

import json

print(json.dumps({"name": "Carl", "age": 56}))
print(json.dumps(["apple", "banana"]))
print(json.dumps(("apple", "mango")))
print(json.dumps("Hello"))
print(json.dumps(9))
print(json.dumps(8.7))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
