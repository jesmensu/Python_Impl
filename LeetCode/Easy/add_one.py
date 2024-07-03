digits = [1,2,3]
def a(digits):
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits

print(a([1, 2, 3, 9]))


# digits = [9,9,0]
# lenDigit = len(digits)
# div = 1
# for i in range(1, lenDigit+1):
#     el = digits[-i] + div
#     rem = el%10
#     div = el//10
#     digits[-i] = rem
#     if (i == lenDigit) and (div == 1):
#         digits = [1] + digits

# print(digits)
