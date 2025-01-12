# 2 is a prime number and 1 and less than 1 is not prime.

num = int(input())

is_prime = True

if(num>2):
    mid_num = num // 2
    for i in range(2, mid_num + 2):
        if num%i == 0:
            is_prime = False
            break
elif(num<=1):
    is_prime = False

print("Status prime number: ", is_prime)


# -----------------------------------------------------

num = int(input())

if num == 2:
    print("prime number")
elif(num>1):
    mid_num = num // 2
    for i in range(2, mid_num + 2):
        if num%i == 0:
            print("Not prime number")
            break
    else:
        print("prime number")
else:
    print("Not prime number")



# All the prime number

num = int(input())
for n in range(1,num+1):
    is_prime = True
    if(n>2):
        mid_num = n // 2
        for i in range(2, mid_num + 2):
            if n%i == 0:
                is_prime = False
                break
    elif(n<=1):
        is_prime = False

    if(is_prime):
        print(n)

