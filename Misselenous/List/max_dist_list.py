# distance between two consecutive element
lst = [3, 4, 7, 8, 40, 30, 1]
max_dist = 0
for i in range(len(lst)-1):
    dist = abs(lst[i] - lst[i + 1])
    if max_dist<dist:
        max_dist = dist
        a = lst[i]
        b = lst[i+1]
print(a, b, max_dist)

# max dist between any two element

min_lst = lst[0]
max_lst = lst[0]
for i in lst:
    if i<min_lst:
        min_lst = i
    if i>max_lst:
        max_lst = i

print(min_lst, max_lst, max_lst-min_lst)

# ----------------------------------------
max_dist = 0
for i in range(len(lst)-1):
    for j in range(i+1, len(lst)):
        dist = abs(lst[i] - lst[j])
        if max_dist<dist:
            max_dist = dist
            a = lst[i]
            b = lst[j]
print(a, b, max_dist)
