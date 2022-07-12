t = int(input())
while t != 0:
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    min = a[0] ^ a[1]
    for i in range(1, n-1):
        val = a[i] ^ a[i+1]
        if val < min:
            min = val
    print(min)
    t -= 1