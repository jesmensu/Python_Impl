nums = [2,7,11,15,76,99,100] 
target = 26

def get_two_sum_for_target(nums, target):
    if len(nums) == 0:
        return None
    first_index = 0
    sec_index = len(nums) -1
    while(sec_index>first_index):
        temp = target - nums[first_index]
        if nums[sec_index] == temp:
            return (nums[first_index], nums[sec_index])
        if nums[sec_index] < temp:
            first_index += 1
        else:
            sec_index -= 1

    return None, None

def get_two_sum_for_target1(nums, target):
    if len(nums) == 0:
        return None, None
    first_index = 0
    sec_index = len(nums) -1
    while(sec_index>first_index):
        sum = nums[first_index] + nums[sec_index]
        if sum == target:
            return nums[first_index], nums[sec_index]
        elif sum < target:
            first_index += 1
        else:
            sec_index -= 1
        
def get_sub_for_target1(nums, target):
    if len(nums) == 0 or target <= 0:
        return None, None
    first_index = 0
    sec_index = 1
    while(first_index <= sec_index < len(nums)):
        sub = nums[sec_index] - nums[first_index]
        if sub == target:
            return first_index, sec_index
        elif sub < target:
            sec_index += 1
        else:
            first_index += 1

if __name__ == "__main__":
    nums = [2,7,11,15,76,99,100] 
    target = 4
    print(get_sub_for_target1(nums,target))