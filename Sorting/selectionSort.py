a = [23,78,45,8,23,32,46]

def selectionSort(a):
    for i in range(len(a)-1):
        minNum = a[i]
        minIndex = i
        for j in range(i+1,len(a)):
            if a[j] < minNum:
                minNum = a[j]
                minIndex = j
        a[i], a[minIndex] = a[minIndex], a[i] 

selectionSort(a)
print(a)
