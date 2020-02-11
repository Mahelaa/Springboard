#Parse Dataset into managable chunks

import json

store = {}

with open('/Users/terminus/Downloads/Models/reviews_Electronics_5.json') as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}


print(data)