def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    result = [[0 for j in range(n)] for i in range(n)]
    counter = 1
    top, left, bottom, right = 0,0,n-1,n-1
    while counter <= n*n:
        for j in range(left, right + 1):
            if(counter > n*n): break;
            result[top][j] = counter
            counter += 1
        top += 1 
        for i in range(top, bottom + 1):
            if(counter > n*n): break;
            result[i][right] = counter
            counter += 1
        right -= 1
        for j in range(right, left - 1, -1):
            if(counter > n*n): break;
            result[bottom][j] = counter
            counter += 1
        bottom -= 1
        for i in range(bottom, top - 1, -1):
            if(counter > n*n): break;
            result[i][left] = counter
            counter += 1        
        left += 1
    return result

print(generateMatrix(4))