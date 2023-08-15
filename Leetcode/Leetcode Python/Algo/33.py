from math import inf

nums = [4,5,6,7,8,1,2,3]
target = 8

def search(nums, target):
    if target == nums[0]: return 0
    left = 0
    right = len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        if nums[mid] == target: return mid
        else:
            mid_val = nums[mid]
            if target < nums[0] and mid_val >= nums[0]: mid_val = -inf
            elif target > nums[0] and mid_val < nums[0]: mid_val = inf
            if target < mid_val: right = mid - 1
            else: left = mid + 1  
    return -1

print(search(nums, target))