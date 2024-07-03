# missing element from the sequence of n consecutive unique element

n = 7
sum_of_n_sec = n*(n+1)/2
lst = [2,1,7,4,6,5]
sum_of_lst = sum(lst)

missing_elem = sum_of_n_sec - sum_of_lst
print(missing_elem)