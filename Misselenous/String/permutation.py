
# Function to find permutations of a given string
from itertools import permutations
 
def allPermutations(str):
      
     # Get all permutations of string 'ABC'
     permList = permutations(str)             
     permList = [i for i in permList]
     return permList
permList = allPermutations([1,2,3])
print(permList)