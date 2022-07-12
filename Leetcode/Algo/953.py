words = ["hello","leetcode"] 
order = "hlabcdefgijkmnopqrstuvwxyz"

# def isAlienSorted(words,order):
#     for i in range(len(words) - 1):
#         for j in range(len(words[i])):
#                 if j >= len(words[i + 1]): return False
#                 if words[i][j] != words[i + 1][j]:
#                     if order.find(words[i][j]) > order.find(words[i + 1][j]): 
#                         return False
#                     break
#     return True

def isAlienSorted(words,order):
    size = len(words)
    prev_word = words[0]
    prev_len = len(prev_word) 
    for i in range(1, size):
        curr_len = len(words[i])
        min_len = min(prev_len, curr_len)
        break_flag = False
        for j in range(min_len):
            order_prev_index = order.find(prev_word[j])
            order_curr_index = order.find(words[i][j])
            if order_prev_index < order_curr_index: 
                break_flag = True 
                break
            elif order_prev_index > order_curr_index:
                return False
        if (not break_flag) and prev_len != min_len: return False
        prev_word = words[i]
        prev_len = curr_len
    return True

ans = isAlienSorted(words, order)
print(ans)    