lst = [78,2,3,74,74,1,6,89,56,34,89]

min_lst = lst[0]
max_lst = lst[0]
for i in lst:
    if i<min_lst:
        min_lst = i
    if i>max_lst:
        max_lst = i

print(min_lst, max_lst, max_lst-min_lst)

# Second maximum
sec_max_lst = lst[0]
max_lst = lst[0]
for i in lst:
    if max_lst == i:
        continue
    if i>max_lst:
        sec_max_lst = max_lst
        max_lst = i
        continue
    if i>sec_max_lst:
        sec_max_lst = i

print(sec_max_lst, max_lst)

# with sort
lst = list(set(lst))
lst.sort(reverse= False)
sec_max_lst = lst[-2]
print(sec_max_lst)

# find nth largest
max_lst = lst[0]
num = int(input("Enter the n: "))
list_elmt = []
for n in range(num):
    max_lst = lst[0]
    for i in lst:
        if i>=max_lst:
            max_lst = i
    list_elmt.append(max_lst)
    lst.remove(max_lst)

print(list_elmt)

final_list = []

for i in range(0, 2):
    max1 = 0

    for j in range(len(lst)):
        if lst[j] > max1:
            max1 = lst[j]

    lst.remove(max1)
    final_list.append(max1)

print(final_list)