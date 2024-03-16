#  Binary search
lst = [23, 21, 45, 98, 31]
lst.sort()

print(lst)
k = 100

start = 0
end = len(lst)-1
mid = end//2
while(start <= end):
    mid = (start + end) // 2
    if k<lst[mid]:
        end = mid-1
    elif k>lst[mid]:
        start = mid+1
    else:
        print(k, "is in position ", mid)
print(k, "is not in the list")


# With recursion
def binary_search(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        return -1
 
# Test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

result = binary_search(arr, 0, len(arr)-1, x)
print(result)