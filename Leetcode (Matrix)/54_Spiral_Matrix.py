def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    row, col = len(matrix), len(matrix[0])
    counter = row * col
    top, left, bottom, right = 0, 0, row - 1, col - 1
    while counter > 0:
        for j in range(left, right + 1):
            if(counter==0): break
            result.append(matrix[top][j])    
            counter -= 1
            
        top += 1    
        for i in range(top, bottom + 1):
            if(counter==0): break
            result.append(matrix[i][right])
            counter -= 1
            
        right -= 1
        for j in range(right, left - 1, -1):
            if(counter==0): break
            result.append(matrix[bottom][j])
            counter -= 1
            
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            if(counter==0): break
            result.append(matrix[i][left])
            counter -= 1
            
        
        left += 1
    print(counter)
    return result

print(spiralOrder([[1,2,3],[4,5,6]]))