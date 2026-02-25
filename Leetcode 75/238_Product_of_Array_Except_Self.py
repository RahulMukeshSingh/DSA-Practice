class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_len = len(nums)
        right_product = [1] * num_len
        for i in range(num_len - 2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
        left_product = 1
        for i in range(num_len):
            right_product[i]=left_product * right_product[i]
            left_product = left_product * nums[i]
        return right_product
    
s = Solution()
nums = [-1,1,0,-3,3]
print(s.productExceptSelf(nums))