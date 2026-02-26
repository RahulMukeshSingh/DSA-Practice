class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return None
        left_pointer = 0
        right_pointer = len(height) - 1
        max_amt = 0
        while left_pointer < right_pointer:
            width_val = right_pointer - left_pointer
            if height[left_pointer] < height[right_pointer]:
                current_amt = height[left_pointer] * width_val
                left_pointer += 1
            else: 
                current_amt = height[right_pointer] * width_val
                right_pointer -= 1
            if current_amt > max_amt: max_amt = current_amt
        return max_amt
    
sol = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(sol.maxArea(height))