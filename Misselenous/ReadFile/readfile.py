import json
# JSON file
f = open ('Misselenous/ReadFile/data.json', "r")
# Reading from file
# json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary
data = json.loads(f.read())
print(data)
print(type(data))

# json.load() takes a file object and returns the json object or dictionary
f = open ('Misselenous/ReadFile/data.json', "r")
data1 = json.load(f) 
print(data1)
print(type(data1))


j_string = '{"name": "Bob", "languages": "English"}'
 
# deserializes into dict and returns dict.
y = json.loads(j_string)
 
print("JSON string = ", y)

with open("Misselenous/ReadFile/sample.json", "w") as outfile:
    json.dump(y, outfile)

