
from typing import List


def removeConsecDuplicates(nums: List[int]) -> int:
# inplace algo. remove from the same list
    lenNum = len(nums)
    p = 0
    for i in range(lenNum-1):
        if nums[i] != nums[i+1]:
            p = p+1
            nums[p] = nums[i+1]

    return nums, p+1


def removeConsecDuplicates1(nums: List[int]) -> int:
    i = 0
    while i < (len(nums)-1):
        if nums[i] == nums[i+1]:
            del nums[i]
            continue
        i = i+1
    return nums, len(nums)

def removeConsecDuplicates2(nums: List[int]) -> int:
    n = 0
    while n < len(nums)-1:
        if nums[n] == nums[n+1]:
            del nums[n]
            n-=1
        n+=1
    return len(nums)

nums = [0, 0, 1, 3, 3, 3, 4, 5,3]

print(removeConsecDuplicates1(nums))