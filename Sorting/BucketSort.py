from math import floor

a = [0.04,0.12,0.17,0.132,0.15,0.35,0.43,0.50]

def fillBucket(a):
    buckets = [[],[],[],[],[],[],[],[],[],[]]
    for num in a:
        index = floor(num * 10)
        bucket = buckets[index]
        flag = False
        i = 0
        for i in range(len(bucket)):
            if(bucket[i] >= num):
                flag = True
                break    
        if flag: 
            bucket.insert(i, num)
        else:   
            bucket.append(num)
    return buckets        

def bucketSort(a):
    sortedList = []
    buckets = fillBucket(a)
    for bucket in buckets:
        for num in bucket:
            sortedList.append(num)
    return sortedList        

sortedList = bucketSort(a)
print(sortedList)
