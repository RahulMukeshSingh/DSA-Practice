def bubble_sort(a):
    swapped = False
    size_a = len(a)
    for i in range(size_a):
        for j in range(size_a - i - 1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swapped = True
        if not swapped: #If no swapping occured
            break

a = list(range(10,0,-1))
print(a)
bubble_sort(a)
print(a)            



