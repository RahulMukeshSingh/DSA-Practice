# t = int(input())
# while t!=0:
#     n,k = map(int, input().split())
#     arr = list(map(int, input().split()))
#     index = n - (k%n)
#     for i in range(index, n):
#         print(arr[i], end = " ")
#     for i in range(index):    
#         print(arr[i], end = " ")
#     print("")
#     t-=1
        
# 1
# 5 2
# 1 2 3 4 5

T = int(input())
while T != 0:
    N, K = map(int, input().split(" "))
    A = list(map(int,input().split(" ")))
    index = N - (K % N)
    for i in range(index, N):
        print(A[i], end = " ")
    for i in range(index):
        print(A[i], end = " ")
    print()    
    T -= 1        