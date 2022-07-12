from math import floor
def search(nums, target):
    start = 0
    end = len(nums) -1
    index = -1
    while start <= end:
        mid = floor((start + end)/2)
        if nums[mid] == target:
            index = mid
            break
        elif target > nums[mid]:
            start = mid + 1
        else:
            end = mid - 1       
    if index == -1: return [-1,-1]
    ans = [index, index]
    last = len(nums) - 1
    prevIndex = index
    nextIndex = index
    prevFlag = nextFlag = True
    while prevFlag or nextFlag:
        if nums[prevIndex] != target: prevFlag = False
        if nums[nextIndex] != target: nextFlag = False
        if nums[prevIndex] == target and prevFlag:
            if prevIndex == 0: prevFlag = False
            ans[0] = prevIndex
            prevIndex = max(0, prevIndex - 1)
        if nums[nextIndex] == target and nextFlag:
            if nextIndex == last: nextFlag = False
            ans[1] = nextIndex     
            nextIndex = min(nextIndex + 1, last)
    return ans

print(search([3,3,3],3))     