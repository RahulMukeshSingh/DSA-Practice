nums = [2,7,11,15] 
target = 9
def twoSum(nums, target):
    nums = [[val,i] for i, val in enumerate(nums)]
    print(nums)
    nums.sort()
    left = 0
    right = len(nums) - 1
    while(left < right):
        sum = nums[left][0] + nums[right][0]
        if sum == target:
            return [nums[left][1],nums[right][1]]
        elif sum > target: right -= 1
        else: left += 1
    return [-1,-1]
twoSum(nums,target)

def twoSumIndex(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        next_val = target - num
        if next_val in lookup: return [i,lookup[next_val]]
        lookup[num] = i       
