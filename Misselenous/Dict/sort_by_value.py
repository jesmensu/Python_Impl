list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
 

print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: (i['age'],i['name'])))
print(sorted(list, key=lambda i: i.keys()))


d = {'aa': 10, 'ba': 8, 'db': 6, 'ce': 4}
# sort dict with values
d1 = sorted(d.items(), key = lambda x: x[1])
print(d1)

# sort dict with keys
d1 = sorted(d.items(), key = lambda x: x[0])
print(d1)

d = {'a': 10, 'b': 8, 'd': 6, 'c': 4}
d1 = sorted(d, key = d.get)
print(d1)

