# def findPeakElement(nums):
#     size = len(nums)
#     if size == 1: return 0
#     for i in range(size):
#         if i == 0 and nums[i] > nums[i+1]: return i 
#         if i == size - 1 and nums[i] > nums[i-1]: return i
#         if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]: return i
#     return -1

from math import inf


def findPeakElement(nums):
    left = 0
    right = len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        direct_left = -inf if mid <= 0 else nums[mid - 1]
        direct_right = -inf if mid >= (len(nums) - 1) else nums[mid + 1]
        if nums[mid] > direct_right and nums[mid] > direct_left: return mid
        elif nums[mid] > direct_left: left = mid + 1
        else: right = mid - 1
    return -1    