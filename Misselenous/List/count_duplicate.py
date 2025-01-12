lst = [1, 5, 3, 8, 5, 3]

d = {}

for i in lst:
    d[i] = d.get(i, 0) + 1

s = sum([k for k, v in d.items() if v != 1])

print(s)
