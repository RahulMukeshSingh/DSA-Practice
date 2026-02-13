class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        positive_index = -1
        negative_index = -1

        while len(asteroids) > 0:
            positive_index = -1
            negative_index = -1
            for i in range(1,len(asteroids)):
                if asteroids[i] < 0 and asteroids[i-1] > 0:
                    positive_index = i-1
                    negative_index = i
                    break
            if(positive_index != -1 and negative_index != -1):
                delta = asteroids[positive_index] + asteroids[negative_index]
                if delta == 0:
                    asteroids.pop(negative_index) 
                    asteroids.pop(positive_index)      
                elif delta < 0:
                    asteroids.pop(positive_index)
                else:
                    asteroids.pop(negative_index)
            else:
                break
            
        return asteroids                     
                

sol = Solution()
input_data = [5, 10, -5]
result = sol.asteroidCollision(input_data)
print(f"Remaining asteroids: {result}")