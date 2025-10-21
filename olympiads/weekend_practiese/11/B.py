import sys
from math import isqrt
n_str = sys.stdin.readline()
n = int(n_str)

r = n%10
used = n - r
# def sieve(n: int) -> list[int]:
#     """Return a list of all primes ≤ n using Sieve of Eratosthenes."""
#     if n < 2:
#         return []
#     sieve = bytearray(b"\x01") * (n + 1)
#     sieve[0:2] = b"\x00\x00"  # 0 and 1 are not primes
#     for p in range(2, int(n**0.5) + 1):
#         if sieve[p]:
#             sieve[p*p:n+1:p] = b"\x00" * ((n - p*p)//p + 1)
#     return [i for i in range(2, n + 1) if sieve[i]]
a = []
ans = 0

for i in range(r+1, isqrt(n)+1):
    if used % i == 0:
        # print(i)
        ans+=1
        a.append(i)
        j = used // i
        if j != i and j > r:
            ans+=1
            a.append(j)

print(ans)
print(*a)