from math import inf

minCount = inf

def sumSubsequence(coins, amount, currSum = 0, count = 0):
    if currSum == amount: return min(count, minCount)
    if currSum > amount: return 0
    size = len(coins)
    for i in range(size):
        count += sumSubsequence(coins, amount, currSum + coins[i], count)
    return count

def coinChange(coins, amount, currSum = 0):
    
    sum = sumSubsequence(coins, amount)
    if sum == 0: return -1
