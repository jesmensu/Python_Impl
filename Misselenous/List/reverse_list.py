lst = [1,1,3,4,5, 1]
l = len(lst)
for i in range(l//2):
    if(lst[i]!= lst[l-i-1]):
        lst[i], lst[l-i-1] = lst[l-i-1], lst[i]
print(lst)

# -------------------------------------------
lst = [1,2,3,4,5]
lst = lst[::-1]
print(lst)

# -------------------------------------------
lst = [1,2,3,4,5]
l = len(lst)
lst_rev = []
for i in range(1, l+1):
    lst_rev.append(lst[-i])
print(lst_rev)

# -------------------------------------------
lst = [1,2,3,4,5]
l = len(lst)
lst_rev = []
for i in lst:
    lst_rev.insert(0,i)
print(lst_rev)