import collections


nums = [3,3,3,2,2,1,1,1,2,2]
def majorityElement(nums):
    candidate = None
    count = 0
    for n in nums:
        if count == 0: candidate = n
        count += (1 if candidate == n else -1)
    return candidate   

majorityElement(nums)    