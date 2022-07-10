from math import floor

a = [5, 7, 8, 9, 25, 36, 37]

def binarySearch(a, value):
    start = 0
    end = len(a) - 1
    while start <= end:
        mid = floor((start + end)/2)
        if a[mid] == value: return mid
        elif value > a[mid]: start = mid + 1
        else: end = mid - 1
    return -1

for v in a:
    print(binarySearch(a,v))

print(binarySearch(a,27))    


