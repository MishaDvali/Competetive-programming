import math
from collections import defaultdict
import itertools
def is_prime(n: int):
    if n ==2 or n==1 or n==3:
        return True
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [1]


for i in range(2, 30):
    if is_prime(i):
        primes.append(i)
print("Primes are filled")


def find_smallest_prime(n: int):
    for prime in primes:
        if n % prime == 0:
            return prime
    print("No prime found")


def find_prime_divisors(n):
    if n in primes: 
        return [n]
    divisors = []
    while True:
        smallest_prime = find_smallest_prime(n)
        print(divisors, n, smallest_prime)
        if smallest_prime == n:
            divisors.append(smallest_prime)
            break
        divisors.append(smallest_prime)
        n = n / smallest_prime
    print(divisors)
    return divisors

def C_n_k(n, k):
    return math.factorial(n)/(math.factorial(n-k) * math.factorial(k))

def how_many_repeats(divisors):
    met = defaultdict(lambda: 0)
    for divisor in divisors:
        met[divisor]+=1
    return met, divisors

def count(stuff):
    divisors = stuff
    perms = itertools.permutations(divisors)
    ans = set()
    amount_of_divisors = len(divisors)
    for perm in perms:
        print(f"FOR PERM {perm}:")
        for i in range(amount_of_divisors):
            val = math.prod(perm[:i])
            ans.add(val)
            print(val)

k = int(input())

i = 2
print(find_prime_divisors(4))
while True:
    print(f"FOR NUMBER {i}")
    ans = count(find_prime_divisors(i))
    if k == ans:
        print(f"ANSWER: {i}")
        break
    i+=1
