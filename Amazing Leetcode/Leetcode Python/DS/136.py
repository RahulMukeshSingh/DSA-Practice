def singleNumber(nums):
    ans = nums[0]
    for i in range(1, len(nums)):
        ans ^= nums[i]
    return ans    