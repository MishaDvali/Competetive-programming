
import math
from typing import Dict, List
import sympy
from collections import defaultdict


# primes = [2, 3]
# def is_prime(n: int):
#     for prime in primes:
#         if n % prime == 0:
#             return False
#     return True
#
# for i in range(4, 2000000):
#     if is_prime(i):
#         primes.append(i)
# print("Primes are filled")
primes: List[int] = list(sympy.primerange(2,2000000))

cache_smallest_prime_divisors: Dict[int, int] = {}
cache_divisors: Dict[int, List[int]] = {}
def find_smallest_prime(n: int) -> int:
    cached = cache_smallest_prime_divisors.get(n) 
    if cached is not None:
        return cached
    root = math.sqrt(n)
    for prime in primes:
        if prime > root:
            break
        if n % prime == 0:
            cache_smallest_prime_divisors[n] = prime
            return prime
    if n in primes:
        cache_smallest_prime_divisors[n] = n
        return n
    print("No prime found")


def find_prime_divisors(n):
    if n in primes: 
        return [n]
    divisors:List[int] = []
    need_to_cache: List[List[int]] = []
    while True:
        cached: List[int] | None = cache_divisors.get(n) 
        if cached is not None:
            for uncashed in need_to_cache:
                uncashed.extend(cached)
            return divisors + cached
        cache_divisors[n] = []
        need_to_cache.append(cache_divisors[n])
        smallest_prime = find_smallest_prime(n)
        # print(divisors, n, smallest_prime)
        divisors.append(smallest_prime)
        for uncached in need_to_cache:
            uncached.append(smallest_prime)
            # print(cache_divisors)
        if smallest_prime == n:
            break
        # print(smallest_prime)
        n = n / smallest_prime
    # print(divisors)
    return divisors


def how_many_repeats(divisors):
    met = defaultdict(lambda: 0)
    for divisor in divisors:
        met[divisor]+=1
    return met

def ans(n) -> int:
    prods = {1}
    divisors = how_many_repeats(find_prime_divisors(n))

    for divisor, exponent in divisors.items():
        new_prods = set()
        for new_exponent in range(exponent + 1):
            for prod in prods:
                new_prods.add(prod * (divisor ** new_exponent))
        prods = new_prods
    ans = len(prods) / 2
    root =  math.sqrt (n)
    if math.floor(root) == root and root in prods:
        ans += 0.5
    # print(prods)
    if int(ans) != ans:
        raise Exception(" Oh no" + str(ans))
    return int(ans)


table = {1:1, 2:4}
i = 3
need_to_cache = set(range(3, 51))
while len(need_to_cache) > 0:
    combinations = ans(i)
    table_val = table.get(combinations)
    if table_val is None:
        if combinations in need_to_cache:
            print(combinations, i)
            table[combinations] = i
            need_to_cache.remove(combinations)
    i+=1
print(table)
