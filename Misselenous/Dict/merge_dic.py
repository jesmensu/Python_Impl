dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict1.update(dict2)
print(dict1)

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

d = dict1|dict2
print(d)

res = {**dict1, **dict2}
print(res)

for k, v in dict2.items():
    dict1[k] = v
print(dict1)