from bisect import bisect_left
from math import ceil
n, k = map(int, input().split())
s = [int(input()) for _ in range(n)]
s.sort()
def solve(n, k, s):
    s_sum = sum(s)
    if k > s_sum:
        return 0
    minl = 1
    maxl = s_sum
    while minl < maxl:
        midl = ceil((minl+maxl)/2)
        how_many_can_get = 0
        for i in range(bisect_left(s, midl), n):
            how_many_can_get += s[i] // midl
        can_divide = how_many_can_get >= k
        if can_divide:
            minl = midl
        else:
            maxl = midl-1
    return minl
print(solve(n, k, s))
