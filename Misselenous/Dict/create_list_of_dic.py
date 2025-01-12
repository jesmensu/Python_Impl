# Convert dict to list of dict
test_dict = {'Apple' : [5, 6, 7, 8],
            'Banana' : [10, 11, 7, 5],
            'Berry' : [6, 12, 10, 8],
            'Grapes' : [1, 2, 5]}

new_list = []
for key, value in test_dict.items():
    if not new_list:
        for v in value:
            new_dic = {}
            new_dic[key] = v
            new_list.append(new_dic)
    else:
        for v, item in zip(value,new_list):
            item[key] = v

print(new_list)

# Another approach
new_dic = []
for key, value in test_dict.items():
    for i in range(len(value)):
        if len(new_dic) == i:
            dic = {}
            new_dic.append(dic)
            new_dic[i][key] = value[i]
        else:
            new_dic[i][key] = value[i]
print(new_dic)

# convert list of dict to dict of list value
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

new_dict = {}
for dic in new_list:
    for key, value in dic.items():
        if key in new_dict:
            new_dict[key].append(value)
        else:
            new_dict[key] = [value]

print(new_dict)
