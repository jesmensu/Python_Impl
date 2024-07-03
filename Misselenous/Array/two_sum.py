nums = [2,7,11,15,76,99,100] 
target = 26

def get_index_for_sum(num, target):
    first_index = 0
    sec_index = len(num) -1
    while(sec_index>first_index):
        temp = target - num[first_index]
        if num[sec_index] == temp:
            return (first_index, sec_index)
        if num[sec_index] < temp:
            first_index += 1
        else:
            sec_index -= 1


print(get_index_for_sum(nums,target))