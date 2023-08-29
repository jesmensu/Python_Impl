def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        result = n * factorial(n-1)
        return result
    
num = int(input())
result = factorial(num)
print(result)

# Without recursion

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
# Driver Code
num = 5
print("Factorial of",num,"is",
factorial(num))

# ----------------------------------------
