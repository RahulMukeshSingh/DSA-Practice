def setZeroes(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    row, col = len(matrix), len(matrix[0])
    row_marker = [False for i in range(row)]
    col_marker = [False for j in range(col)]
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                row_marker[i] = True
                col_marker[j] = True
    for i in range(row):
        for j in range(col):
            if row_marker[i] or col_marker[j]:
                matrix[i][j] = 0
