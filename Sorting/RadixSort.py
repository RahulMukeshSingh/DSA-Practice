from math import floor, log10
a = [804, 26, 5, 64, 52, 1]

def customBucketSort(a,d):
    buckets = [[],[],[],[],[],[],[],[],[],[]]
    for numStr in a:
        index = int(numStr[d])
        buckets[index].append(numStr)
    i = 0
    for bucket in buckets:
        for numStr in bucket:
            a[i] = numStr
            i += 1    


def radixSort(a):
    maxNum = max(a)
    digits = floor(log10(maxNum)) + 1
    for i in range(len(a)):
        a[i] = str(a[i]).zfill(digits)           
    for d in range(digits - 1, -1, -1):
        customBucketSort(a,d)

radixSort(a)
