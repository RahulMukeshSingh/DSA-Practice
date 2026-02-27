class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Version 1
        # if not nums: return None
        # num_of_element = len(nums)
        # max_num_consecutive_1 = 0
        # left_index = 0
        # right_index = 0
        # no_of_0_slide = 1 if nums[0] == 0 else 0
        # cur_num_consecutive_1 = 0
        # while right_index < num_of_element:  
        #     if no_of_0_slide <= k:
        #         cur_num_consecutive_1 = right_index - left_index + 1
        #         right_index += 1
        #         if right_index < num_of_element and  nums[right_index] == 0: no_of_0_slide += 1
        #     elif no_of_0_slide > k:
        #         if nums[left_index] == 0: no_of_0_slide -= 1
        #         left_index += 1   
        #     if cur_num_consecutive_1 > max_num_consecutive_1: max_num_consecutive_1 = cur_num_consecutive_1 
        # return max_num_consecutive_1
        
        # Version 2
        if not nums: return None
        num_of_element = len(nums)
        max_num_consecutive_1 = 0
        left_index = 0
        right_index = 0
        cur_num_consecutive_1 = 0
        for right_index in range(num_of_element):
            if nums[right_index] == 0: k -= 1
            while k < 0 and left_index <= right_index:
                if nums[left_index] == 0: k += 1
                left_index += 1
            cur_num_consecutive_1 = right_index - left_index + 1
            if cur_num_consecutive_1 > max_num_consecutive_1: max_num_consecutive_1 = cur_num_consecutive_1
        return max_num_consecutive_1
    
sol = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0] 
k = 2
print(sol.longestOnes(nums,k))