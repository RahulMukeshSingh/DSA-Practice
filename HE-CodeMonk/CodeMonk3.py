# t = int(input())
# while t != 0:
#     n,k = list(map(int, input().split()))
#     a = max = input()
#     ans = 0
#     for i in range(1, n):
#         a = "".join([a[1:n],a[0]])
#         if a > max:
#             max = a
#             ans = i
#     a = max
#     k -= 1
#     count = 0
#     while True:
#         a = "".join([a[1:n],a[0]])
#         count += 1
#         if(a == max):
#             break
#     ans = ans + (count * k)    
#     print(ans)
#     t -= 1

t = int(input())
while t != 0:
    n,k = list(map(int, input().split()))
    a = input()
    max = ""
    a_to_max = 0
    max_to_max = -1
    for i in range(n):
        if a > max:
            max = a
            a_to_max = i
        elif a == max:
            max_to_max = i
            break
        a = a[1:] + a[0]
    if max_to_max == -1:
        print(a_to_max + (k-1) * n)
    else:
        print(a_to_max + (k-1) * (max_to_max - a_to_max))        
    t -= 1