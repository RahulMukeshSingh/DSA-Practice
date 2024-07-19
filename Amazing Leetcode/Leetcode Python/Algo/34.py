def searchRange(nums, target):
    if not len(nums): return [-1, -1]
    left = 0
    right = len(nums) - 1
    leftmost = -1
    while(left <= right):
        mid = (left + right) // 2
        if nums[mid] == target:
            leftmost = mid
            right = mid - 1
        elif target > nums[mid]: left = mid + 1
        else: right = mid - 1

    left = rightmost = leftmost
    right = len(nums) - 1
    while(left <= right):
        mid = (left + right) // 2
        if nums[mid] == target:
            rightmost = mid
            left = mid + 1
        elif target > nums[mid]: left = mid + 1
        else: right = mid - 1
    return [leftmost, rightmost]


print(searchRange([3,3,3],3))