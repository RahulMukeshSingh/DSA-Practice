def rearrange(arr, n):
    if len(arr) == 1: return arr
    pos_pointer = 0
    neg_pointer = 1
    for i in range(n):
        if i % 2 == 0 and arr[i] < 0:
            while pos_pointer < n and arr[pos_pointer] < 0: pos_pointer += 1
            if pos_pointer < n and arr[pos_pointer] >= 0: arr[i], arr[pos_pointer] = arr[pos_pointer], arr[i]
        elif i % 2 == 1 and arr[i] >= 0: 
            while neg_pointer < n and arr[neg_pointer] >= 0: neg_pointer += 1
            if neg_pointer < n and arr[neg_pointer] < 0: arr[i], arr[neg_pointer] = arr[neg_pointer], arr[i]
        print(arr, i, pos_pointer, neg_pointer)    
            
arr = [9, 4, -2, -1, 5, 0, -5, -3, 2]
rearrange(arr, len(arr))
print(arr)
#9 -2 4 -1 5 -5 0 -3 2           