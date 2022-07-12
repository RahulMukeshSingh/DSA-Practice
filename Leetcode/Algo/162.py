def findPeakElement(nums):
    size = len(nums)
    if size == 1: return 0
    for i in range(size):
        if i == 0 and nums[i] > nums[i+1]: return i 
        if i == size - 1 and nums[i] > nums[i-1]: return i
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]: return i
    return -1