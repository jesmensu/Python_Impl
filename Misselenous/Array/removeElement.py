def removeElement(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    i = 0
    while i <len(nums):
        if nums[i]==val:
            nums.remove(val)
            i -= 1
        i += 1
    return nums, len(nums)

print(removeElement([0,1,2,2,3,0,4,2], 2))

def removeElement1(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.remove(val)
            continue
        i += 1
    return nums, len(nums)

print(removeElement1([0,1,2,2,3,0,4,2], 2))