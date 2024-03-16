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

# convert list of dict to dict of list value
list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]

new_dict = {}
for l in list:
    if not new_dict:
        for k,v in l.items():
            new_dict[k] = [v]
    else:
        for k,v in l.items():
            new_dict[k].append(v)

print(new_dict)
