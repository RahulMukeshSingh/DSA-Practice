def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    row, col = len(mat), len(mat[0])
    if (r * c) != (row * col):
        return mat

    result = [[0 for j in range(c)] for i in range(r)]
    result_i, result_j = 0, 0
    for i in range(row):
        for j in range(col):
            result[result_i][result_j] = mat[i][j] 
            result_j += 1
            if(result_j == c):
                result_i += 1
                result_j = 0
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
    
result = matrixReshape(matrix,3,2)
print(result)