# String pallindrome
def isPalindrome(str):
    l = len(str)//2
    for i in range(0, l):
        if str[i] != str[-i-1]:
            return False
    return True

print(isPalindrome("weiew"))

# int pallindrome
# def is_palindrome(num):
    