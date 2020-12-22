#Order the Result

import json

x = {"name": "George", "age": 65, "country": "Sweden"}

y = json.dumps(x, indent=2, sort_keys=True)
print(y)
