st = "wggggnnmhhhbkkk"

new_st = ""
l = len(st)
count = 1
for i in range(l-1):  
    if (st[i] == st[i+1]):
        count += 1
    else:
       new_st = new_st + st[i]+ str(count)
       count = 1
new_st = new_st + st[l-1]+ str(count)

print(new_st) 

new_st = ""
prev_s = st[0]
count = 0
for s in st: 
    if prev_s == s:
        count += 1
    else:
       new_st = new_st + prev_s+ str(count)
       count = 1 
    prev_s = s
new_st = new_st + prev_s+ str(count)
print(new_st)

# with while
new_st = ""
count = 1
i = 0
while(i<l-1):  
    if (st[i] == st[i+1]):
        count += 1
    else:
       new_st = new_st + st[i]+ str(count)
       count = 1
    i += 1
new_st = new_st + st[l-1]+ str(count)
print(new_st)

# With dictionary
dict_count = {}
count = 1
i = 0
for i in range(l-1): 
    if (st[i] == st[i+1]):
        count += 1
    else:
       dict_count[st[i]] = count
       count = 1
dict_count[st[i]] = count
print(dict_count)