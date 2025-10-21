cache_with_A = {}
cache_with_B = {}


def find(n: int, put_A: bool):
    if n == 1:
        return 1

    if put_A:
        cacheA = cache_with_A.get(n)
        if cacheA is not None:
            return cacheA
        cache_with_A[n] = find(n-1, False)
        return cache_with_A[n]

    if not put_A:
        cacheB = cache_with_B.get(n)
        if cacheB is not None:
            return cacheB
        cache_with_B[n] = find(n-1, False) + find(n-1, True)
        return cache_with_B[n]

# while True:
#     cache_with_A = {}
#     cache_with_B = {}
    # n = int(input())
    # if n == 1000:
    #     ans =  find(n-2, False) + find(n-2, True)
    #     ans_1 =  find(n-1, False) + find(n-1, True)
    #     print(ans + ans_1)
    # else:
    #     ans =  find(n, False) + find(n, True)
    #     print(ans)
n = int(input())
if n == 1000:
    ans =  find(n-2, False) + find(n-2, True)
    ans_1 =  find(n-1, False) + find(n-1, True)
    print(ans + ans_1)
else:
    ans =  find(n, False) + find(n, True)
    print(ans)
