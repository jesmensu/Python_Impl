# frozenset() function takes a single parameter which can be set, dictionary, tuple, etc.
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

'''Like normal sets, frozenset can also perform different operations like copy, difference, intersection, symmetric_difference, and union.'''
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})
print(A.intersection(B))  # Output: frozenset({3, 4})
print(A.difference(B))  # Output: frozenset({1, 2})
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})
print(A.isdisjoint(C))  # Output: True
print(C.issubset(B))  # Output: True
print(B.issuperset(C))  # Output: True

# When you use a dictionary as an iterable for a frozen set, it only takes keys of the dictionary to create the set.
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:', fSet)
