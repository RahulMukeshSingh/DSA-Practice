from math import floor

def findMin(nums):
    left  = 0
    right = len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        if nums[mid] < nums[0]:
            if nums[mid] < nums[max(left, mid-1)]: return nums[mid]
            right = mid - 1    
        elif nums[mid] >= nums[0]:
            next_num = min(mid + 1, right)
            if nums[mid] > nums[next_num]: return nums[next_num]
            left = mid + 1
    return nums[0]        
        

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
    
