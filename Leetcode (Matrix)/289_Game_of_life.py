def gameOfLife(self, board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    # Using 4 States
    rows, cols = len(board), len(board[0])
    directions = [(-1,-1),(-1,0),(-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]
    for i in range(rows):
        for j in range(cols):
            live_neighbor = 0
            for dir_x, dir_y in directions:
                new_x, new_y = i + dir_x, j + dir_y
                if 0 <= new_x < rows and 0 <= new_y < cols:
                    if(abs(board[new_x][new_y]) == 1): live_neighbor += 1
            if (live_neighbor < 2 or live_neighbor > 3) and board[i][j] == 1: board[i][j] = -1
            if live_neighbor == 3 and board[i][j] == 0: board[i][j] = 2
    for i in range(rows):
        for j in range(cols):
            if board[i][j] > 0: board[i][j] = 1
            else: board[i][j] = 0
