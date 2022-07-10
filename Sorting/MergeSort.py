#float('inf') or math.inf
from math import inf
def merge(a,start,mid,end): #Note:- end is last index
    left = a[start:(mid + 1)]
    right = a[(mid + 1):(end + 1)]
    left.append(inf)
    right.append(inf)
    i = j = 0
    for k in range(start, (end + 1)):
        if left[i] <= right[j]: 
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1

def merge_sort(a,start,end):
   if(start < end):
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid + 1, end)
        merge(a, start, mid, end)

a = list(range(10,0,-1))
print(a)
start = 0
end = len(a) - 1
merge_sort(a,start, end)
print(a)
