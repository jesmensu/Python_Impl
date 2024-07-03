nums = [-1,0,1,2,-1,-4]
lengthNum = len(nums)
sortedSet = []
solutionSet = []
for i in range(lengthNum):
    for j in range(i+1, lengthNum):
        for k in range(j+1, lengthNum):
            if i != j and i != k and j != k and (nums[i] + nums[j] + nums[k] == 0):
                solution = [nums[i], nums[j], nums[k]]
                sortedSol = sorted(solution)
                if sortedSol not in sortedSet:
                    sortedSet.append(sortedSol)
                    solutionSet.append(solution)

print(solutionSet)
print(sortedSet)


Not completed