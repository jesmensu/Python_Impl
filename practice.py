num = int(input())
mid = num // 2
is_prime = True
for i in range(2, mid+2):
    if num%i == 0:
        is_prime = False
        break

print(is_prime)