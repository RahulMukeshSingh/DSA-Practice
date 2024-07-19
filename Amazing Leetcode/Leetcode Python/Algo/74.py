matrix = [[1],[3]]
target = 2

def matrix_index(n, col_size):
    j = n % col_size
    i = (n - j) // col_size
    return [i,j]

def single_index(i,j,col_size):
    return (i * col_size) + j

def search(matrix, target):
    left = 0
    row_size = len(matrix)
    col_size = len(matrix[0])
    right = (row_size * col_size) - 1
    while(left <= right):
        mid = (left + right) // 2
        index = matrix_index(mid,col_size)
        if matrix[index[0]][index[1]] == target: return True
        if target > matrix[index[0]][index[1]]: left = mid + 1
        else: right = mid - 1
    return False

print(search(matrix, target))         