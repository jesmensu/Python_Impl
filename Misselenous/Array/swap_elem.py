#No inplace
arr = [-1,-1,6,1,9,3,2,-1,4,-1]
new_arr = []

for i in range(len(arr)):
    if i in arr:
        new_arr.append(i)
    else:
        new_arr.append(-1)

print(new_arr)


# inplace swap
for i in range(len(arr)):
    if i in arr:
        pos = arr.index(i)
        if i!= pos:
            temp = arr[i]
            arr[i] = arr[pos]
            arr[pos] = temp 

            # arr[i], arr[pos] = arr[pos], arr[i]

print(arr)