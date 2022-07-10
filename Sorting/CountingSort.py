a = [2,2,3,4,1,5,1,5]

def countingSort(a):
    count = {}
    sortedList = []
    #-----Counting------------ 
    for num in a:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    #-----Sorting------------                
    maxNum = max(a)        
    for i in range(maxNum + 1):
        if i in count:
            for times in range(count[i]):
                sortedList.append(i)
    return sortedList            

sortedList = countingSort(a)
print(sortedList)                