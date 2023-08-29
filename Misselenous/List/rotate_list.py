lst = [2,3,4,5,6,7]
n = int(input("Enter the num rotation: "))

for i in range(n):
    lst.append(lst.pop(0))

print(lst)


lst = [0, 1, 2, 3, 4, 5, 6, 7]
n = int(input("Enter the num rotation: "))
lst = lst[n:]+lst[:n]

print(lst)

