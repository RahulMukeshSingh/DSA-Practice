def findDiagonalOrder(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[int]
    """
    result = []
    if not mat: return result
    row, col = len(mat), len(mat[0])
    diagonal_dict = {}
    for i in range(row):
        for j in range(col):
            key = i + j
            if key not in diagonal_dict: diagonal_dict[key] = []
            diagonal_dict[key].append(mat[i][j])                      
    for key_, val_ in diagonal_dict.items():
        if key_ % 2 == 0:
            result.extend(val_[::-1])
        else:
            result.extend(val_)

    return result
mat = [[1,2,3],[4,5,6],[7,8,9]]    
print(findDiagonalOrder(mat))