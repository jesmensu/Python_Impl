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

all_char = set(list(test_str))
print(max_char)

max_freq = 0
for char in all_char:
    if test_str.count(char)>max_freq:
        max_freq = test_str.count(char)
        max_ch = char

print(max_ch, max_freq)