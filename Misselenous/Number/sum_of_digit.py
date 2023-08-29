lst = [12, 67, 98, 34]
def digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //= 10
    return digit_sum
 
def sum_of_digits_list(lst):
    return list(map(digit_sum, lst))
 
print(sum_of_digits_list(lst))