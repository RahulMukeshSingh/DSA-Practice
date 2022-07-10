def spiralOrder(matrix):
    direction = 0
    row_size = len(matrix)
    col_size = len(matrix[0])
    size = row_size * col_size
    i = j = 0
    ans = []
    horizontal_start = vertical_start = 0
    horizontal_end = col_size - 1
    vertical_end = row_size - 1
    for k in range(size):
        ans.append(matrix[i][j])
        if direction == 0: #right
            j = min(j + 1, horizontal_end)
            if j == horizontal_end:
                horizontal_end -= 1
                vertical_start += 1
                direction = 1
            if col_size == 1: i =  min(i + 1, vertical_end)     
        elif direction == 1: #down
            i =  min(i + 1, vertical_end)
            if i == vertical_end:
                vertical_end -= 1
                direction = 2
        elif direction == 2: #left
            j = max(horizontal_start, j - 1)
            if j == horizontal_start:
                horizontal_start += 1
                direction = 3
        elif direction == 3: #up
            i =  max(vertical_start, i - 1)
            if i == vertical_start:
                direction = 0           
    return ans     

matrix = [[3],[2]]      
spiralOrder(matrix)                                                           