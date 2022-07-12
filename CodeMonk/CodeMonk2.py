t = int(input())
while t != 0:
    n = int(input())
    m = list()
    for i in range(n):
        m.append(list(map(int, input().split())))
    count = 0     
    for i in range(n):
        for j in range(n):
            for k in range(i, n):
                for l in range(j, n):
                    if (m[i][j] > m[k][l]):
                        count += 1
    print(count)
    t -= 1