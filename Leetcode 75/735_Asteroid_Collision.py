class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if not asteroids: return []
        output_stack = []
        i = 0
        while i < len(asteroids):
            ast = asteroids[i]
            if not output_stack: 
                 output_stack.append(ast)
                 i += 1
                 continue
            last_element = output_stack[-1] #last element
            delta = last_element + ast
            if ast > 0: 
                output_stack.append(ast)
                i += 1
            elif last_element < 0: 
                output_stack.append(ast)
                i += 1
            elif delta == 0: 
                output_stack.pop()
                i+=1    
            elif delta < 0: output_stack.pop()
            else: i+=1
        return output_stack                                        
                

sol = Solution()
input_data = [5, 10, -5]
result = sol.asteroidCollision(input_data)
print(f"Remaining asteroids: {result}")