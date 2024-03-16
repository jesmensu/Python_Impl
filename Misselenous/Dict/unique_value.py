# Get the unique values from the dictionary values

test_dict = {'gfg' : [5, 6, 7, 8],
            'is' : [10, 11, 7, 5],
            'best' : [6, 12, 10, 8],
            'for' : [1, 2, 5]}
d = set(sum(test_dict.values(), []))
print(d)

new_list = []
for value in test_dict.values():
    new_list.extend(value)

print(list(set(new_list)))

new_list = []
for value in test_dict.values():
    for i in value:
        if i not in new_list:
            new_list.append(i)

print(new_list)