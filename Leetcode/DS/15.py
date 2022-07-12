def threeSum(nums):
    size = len(nums)
    nums.sort()
    ans = []
    for i in range(size - 2):
        if i > 0 and nums[i] == nums[i-1]: continue
        left = i + 1
        right = size - 1
        while(left < right):
            sum_zero = nums[i] + nums[left] + nums[right]
            if sum_zero == 0: 
                ans.append([nums[i],nums[left],nums[right]])
                while(left < right and nums[left]==nums[left+1]): left += 1
                while(left < right and nums[right]==nums[right-1]): right -= 1
                left += 1
                right -= 1
            elif sum_zero > 0: right -= 1
            else: left += 1 
    return ans

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
    