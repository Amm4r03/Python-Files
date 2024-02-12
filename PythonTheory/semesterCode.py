import json

person = '{"name": "Bob", "languages": ["English", "French"]}'

b = json.loads(person)

print(b)

print(b['languages'])