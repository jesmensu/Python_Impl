d = dict([(1,10),(2,20)])
print(d)

d = dict(zip((1,10),(2,20)))
print(d)

# merge dictionary with list value
test_dict = {'month': [1, 2, 3], 'name': ['Jan', 'Feb', 'March']}
res = {test_dict['month'][i]: test_dict['name'][i] for i in range(len(test_dict['month']))}
print("Flattened dictionary:", res)