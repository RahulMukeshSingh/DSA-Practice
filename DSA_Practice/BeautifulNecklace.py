from math import inf
N = 5
M = 4
B = [[2,1,8,9],
    [1,4,3,8],
    [1,1,6,2],
    [3,9,9,6],
    [1,7,2,7]]
def beauty_necklace(i,j):
    beauty_min = inf
    for k in range(M):
        max_stone = max(B[i][k], B[j][k])
        beauty_min = min(beauty_min, max_stone)
    return beauty_min    
        

max_beauty = -inf
for i in range(N):
    for j in range(i,N):
        max_beauty = max(max_beauty, beauty_necklace(i,j))
print(max_beauty)
