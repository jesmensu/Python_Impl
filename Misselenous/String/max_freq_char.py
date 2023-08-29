test_str = "GeeksforGeeks"
print ("The original string is : " + test_str)
 
freq = {}
 
# counting frequency of each character
for char in test_str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
 
# finding the character with maximum frequency
max_char = max(freq, key = freq.get)

print(max_char)