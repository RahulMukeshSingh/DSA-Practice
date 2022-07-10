def partition(a,start,end):
    pivot = a[end] #Last Element
    i = start - 1
    for j in range(start, end):
        if(a[j] <= pivot):
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1],a[end] = a[end],a[i+1]        
    return i + 1

def quick_sort(a,start,end):
    if(start < end):
        pivot_index = partition(a,start,end)
        quick_sort(a, start, pivot_index - 1)
        quick_sort(a, pivot_index + 1, end)    

a = list(range(10,0,-1))
print(a)
start = 0
end = len(a) - 1
quick_sort(a,start, end)
print(a)
    