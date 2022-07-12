nums = [4,5,6,7,8,1,2,3]
target = 8


class Solution:
    def find_pivot(self, mid, nums):
        next = prev = mid
        size = len(nums) - 1
        for i in range(mid+1):
            prev_next = next
            prev_prev = prev
            next = min(size, next+1)
            prev = max(0, prev-1)
            if nums[prev_next] > nums[next]: return prev_next
            if nums[prev_prev] < nums[prev]: return prev
        return -1

    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        mid = (left + right) // 2
        pivot = self.find_pivot(mid, nums)
        print(pivot)       
        if pivot != -1:
            nums = nums[pivot + 1:] + nums[0:pivot + 1]
        while(left <= right):
            mid = (left + right) // 2     
            if target == nums[mid]: return (mid + pivot + 1) % len(nums)
            if target < nums[mid]: right -= 1
            else: left += 1
        return -1

print(Solution().search(nums, target))