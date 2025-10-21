from collections import defaultdict
from functools import wraps
import math

def is_prime(n: int):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = []


for i in range(2, 30):
    if is_prime(i):
        primes.append(i)


def find_smallest_prime(n: int):
    if n in primes:
        return n
    for prime in primes:
        if n % prime == 0:
            return prime
    print("No prime found")


def find_prime_divisors(n):
    if n in primes: 
        return 2
    divisors = []
    while True:
        smallest_prime = find_smallest_prime(n)
        print(divisors, n, smallest_prime)
        if smallest_prime == n:
            divisors.append(smallest_prime)
            break
        divisors.append(smallest_prime)
        n = n / smallest_prime
    return divisors

def C_n_k(n, k):
    return math.factorial(n)/(math.factorial(n-k) * math.factorial(k))

def how_many_repeats(divisors):
    repeated = []
    last_devisor = divisors[0]
    repeats = 1
    for divisor in divisors:
        if divisor != last_devisor:
            last_devisor = divisor
            repeats = 1
            continue
        repeats += 1

# def how_many_ways_to_divide(n):
#     divisors = find_prime_divisors(n)
#     s = 1
#     for i in range(1, len(divisors) + 1):
#         s +=C_n_k(len(divisors), i)
#     return s



print("primes:", primes)
print("seqragate number 12:", find_prime_divisors(12))

k = int(input())
print(how_many_ways_to_divide(k) / 2)
# def prime
#
# def find_smallest_divisible_prime(n: int):
#
# def 
