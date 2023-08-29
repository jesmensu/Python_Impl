num = int(input())
rev_num = 0
while(num>=1):
    val = num%10
    num = num//10
    rev_num = rev_num*10 + val

print(rev_num)

