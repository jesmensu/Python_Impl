nums = [1,1,2,2,2,2,3]
def mej(nums):
    count = 0
    candidate = 0

    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate
print(mej(nums))