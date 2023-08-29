
text = "Geeks welcome to the Geeks Kingdom!"


if "Geek" in text:
    print("Substring found!")

st_list = text.split(" ")
if "Geek" in st_list:
    print("Word found!")


# -----------------------------------------
string = "geeks quiz practice code"
# reversing words in a given string
s = string.split()[::-1]
# l = []
# for i in s:
#     l.append(i)
print(" ".join(s))