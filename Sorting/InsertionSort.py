#a[j], a[i] = a[i], a[j] -> swap (don't work in numpy multidimensional array)
# k = list(a) where a is also a list. In order to avoid call by object reference in python inside function
def insertion_sort(a):
    size = len(a)
    for i in range(1, size):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1 
        a[j + 1] = key
    return a    

a = [7,6,5,4,3,2,1]
insertion_sort(a)
print(a)