from math import inf

def findMin(nums):
    left = 0
    right = len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        direct_left = max(0, mid - 1)
        if nums[mid] < nums[direct_left]: return nums[mid]
        elif nums[mid] < nums[0]: right = mid - 1
        else: left = mid + 1
    return nums[0] #No rotation        

print(findMin([11,13,15,17]))


# def findMin(nums):
#     left, right = 0, len(nums)-1
#     while left < right: #not <= as both rleft and right will become same in this case
#         mid = (left + right) // 2
#         if nums[mid] > nums[right]: 
#             left = mid + 1
#         else:
#             right = mid
#     return nums[left]

# print(findMin([11,13,15,17]))    
    
