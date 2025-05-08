def degree_90(matrix):
    # result -> matrix
    # 0,0 -> 2,0
    # 0,1 -> 1,0
    # 0,2 -> 0,0

    # (n - 1 - j),i
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n/2): #Reverse the rows
        matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
    for i in range(n): #Transpose the matrix (swap rows and columns)
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

#Test
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    
degree_90(matrix)
print(matrix)