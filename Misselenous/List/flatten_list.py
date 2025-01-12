

def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
 
nested_list = [[1, 2, 3], [4, [5, 6]], [7, 8]]
flattened_list = flatten_list(nested_list)
 
print(flattened_list)
