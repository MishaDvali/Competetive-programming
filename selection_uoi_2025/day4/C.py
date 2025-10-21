from math import isqrt
from typing import List
n, amount_of_t = list(map(int, input().split()))
tramplines: List[List[int]] = [None for _ in range(amount_of_t+1)]
tramplines[amount_of_t] = [n, n, isqrt(2*(n**2)), 2*n]
for i in range(amount_of_t):
    x1, y1, x2, y2 = list(map(int, input().split()))
    d1 = isqrt(x1**2+y1**2)
    p = x1+y1
    d2 = isqrt(x2**2+y2**2)
    tramp = [x1, y1, d1, p, x2, y2, d2]
    tramplines[i]=tramp
    
tramplines.sort(key=lambda o: o[2])
# print(tramplines)
# print(t)
for ti1 in range(amount_of_t):
    # print(f"FOR TRAMPLINE {ti1}")
    first_tramp = tramplines[ti1]
    x1, y1, d1, p, x2, y2, d2 =first_tramp
    # print("x1, y1, d1, p1, x2, y2, d2")
    # print(x1, y1, d1, p, x2, y2, d2)
    
    for ti2 in range(ti1+1, amount_of_t+1):
        second_tramp = tramplines[ti2]
        if second_tramp[0] < x2 or second_tramp[1] < y2:
            continue
        second_tramp[3]=min(second_tramp[3], p + (second_tramp[0] -x2) + (second_tramp[1]-y2))
# [print(t) for t in tramplines]
print(tramplines[amount_of_t][3])





