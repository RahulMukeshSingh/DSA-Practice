def threeSum(nums):
    nums.sort()
    triplets = []
    def twoSum(left, x):
        right = len(nums) - 1
        while left < right:
            sum = x + nums[left] + nums[right]
            if sum == 0: 
                triplets.append([x, nums[left], nums[right]])
                while left < right and  nums[left] == nums[left + 1]: left += 1
                while left < right and  nums[right] == nums[right - 1]: right -= 1
                left += 1
                right -= 1
            elif sum > 0: right -= 1
            else: left += 1    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        twoSum(i + 1, nums[i])          
    return triplets

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
    