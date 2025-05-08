def transpose(matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row = len(matrix)
        col = len(matrix[0])
        result = [[matrix[j][i] for j in range(row)] for i in range(col)]
        return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    
result = transpose(matrix)
print(result)