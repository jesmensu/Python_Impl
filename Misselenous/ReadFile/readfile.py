import json
# JSON file
f = open ('Misselenous/ReadFile/data.json', "r")
# Reading from file
data = json.loads(f.read())

print(data)


j_string = '{"name": "Bob", "languages": "English"}'
 
# deserializes into dict and returns dict.
y = json.loads(j_string)
 
print("JSON string = ", y)

