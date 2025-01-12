def count_digit(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

count = 10
while(count):
    num_inp = int(input())
    digit = count_digit(num_inp)
    num = num_inp
    new_num = 0
    while(num>=1):
        val = num%10
        num = num//10
        new_num = new_num + val**digit

    if new_num == num_inp:
        print("Amstrong number")
    else:
        print("Not Amstrong number")
    count = count -1

num_i = 500
for i in range(1, num_i+1):
    digit = count_digit(i)
    num = i
    new_num = 0
    while(num>=1):
        val = num%10
        num = num//10
        new_num = new_num + val**digit

    if new_num == i:
        print(i)

