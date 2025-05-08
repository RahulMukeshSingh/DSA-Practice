def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix: return False
    row, col = len(matrix), len(matrix[0])
    left, right = 0,  row * col - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = matrix[mid // col][mid % col]
        if mid_value == target: return True
        elif target < mid_value: right = mid - 1
        else: left = mid + 1 
    return False