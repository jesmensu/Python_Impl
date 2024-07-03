def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    lenNums = len(nums)
    start = 0
    end = lenNums -1
    # if(target < nums[0]):
    #     return 0
    # elif(target > nums[end-1]):
    #     return lenNums
    
    while(start<=end):
        mid = ((end - start) // 2) + start
        if nums[mid] == target:
            return mid
        elif(target > nums[mid]):
            start = mid + 1
        elif(target < nums[mid]):
            end = mid - 1
        
    return start

print(searchInsert([1,2,3,5,9], 0))
