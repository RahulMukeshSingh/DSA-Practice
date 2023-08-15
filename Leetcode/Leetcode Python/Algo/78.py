def subsets(nums):
    subset = [[]]
    for num in nums:
        new_subsets = []
        for curr in subset:
            #subset += [curr + [num] for curr in subset]
            next = curr[:]
            next.append(num)
            new_subsets.append(next)
        subset.extend(new_subsets)
    return subset

def subsets_backtracking(nums):
    subset = [[]]
    def backtracking(nums, curr = []):
        pass


nums = [1,2,3]
print(subsets(nums))   