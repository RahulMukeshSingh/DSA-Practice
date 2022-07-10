def construct2DArray(original, m, n):
    size = len(original)
    if (m * n) != size: return [] 
    matrix = []
    firstColIndex = 0
    lastColIndex = n 
    for i in range(m):
        matrix.append(original[firstColIndex:lastColIndex])
        firstColIndex = lastColIndex
        lastColIndex += n
    return matrix