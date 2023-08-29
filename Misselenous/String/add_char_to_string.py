num = "167852564789.67988"
num_list = num.split(".")
for i in range(3, len(num_list[0]), 4):
    num_list[0] = num_list[0][:-i] + "," + num_list[0][-i:]

print("".join([num_list[0],".",num_list[1]]))

num_list = num.split(".")
digit_list = list(num_list[0])
for i in range(3, len(digit_list), 4):
    digit_list.insert(-i,",")
digit_list.append(".")
num_list[0] = "".join(digit_list)
print("".join(num_list))