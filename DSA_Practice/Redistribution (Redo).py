mod = 1000000007 #10^9 + 7
inputSum = 90
memory = {}

def sumSubsequence(currSum = 0):
    if currSum == inputSum: return 1
    if currSum > inputSum: return 0
    if currSum in memory: return memory[currSum]
    count = 0
    for i in range(3, inputSum + 1, 2):
        count += sumSubsequence(currSum + i)
    count = count % mod    
    memory[currSum] = count    
    return count

print(sumSubsequence())
