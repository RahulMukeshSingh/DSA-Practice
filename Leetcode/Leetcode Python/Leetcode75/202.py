from collections import deque
def happy(n):
    while(n > 1):
        not_happy = deque()
        while(n not in not_happy):
            not_happy.append(n)
            sum_val = 0
            while(n > 0):
                d = n % 10
                sum_val += d * d 
                n = n // 10
            if sum_val == 1: return True
            n = sum_val
        return False      

happy(19)
        