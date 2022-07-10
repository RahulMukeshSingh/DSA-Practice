from math import sqrt, floor
mod = 1000000007
a = [2,3,5,9]
fact = {0:1}
def factorial():
    last_fact = 1
    for i in range(1,100005): # 100005 is maximum size of a
        last_fact = (last_fact * i) % mod
        fact[i] = last_fact

def is_prime(i):
    if i < 2: return False
    if i == 2: return True
    last = floor(sqrt(i))
    for d in range(2,last + 1):
        if i % d == 0: return False
    return True

factorial()
prime_numbers = list(filter(is_prime, a))
n = len(prime_numbers)
count = n
for r in range(2,n+1):
    count = (count + (fact[n] / fact[n-r])) % mod
print(floor(count))    