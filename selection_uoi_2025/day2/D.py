n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]

dp = [0 for _ in range(n+1)]


def calc(a, fr, dp, n):
    for i in range(fr, n):
        # print()
        # print("i", i)
        maximum_dp = 0
        maximum = a[i]
        minimum = a[i]
        for j in range(i-1, -1, -1):
            maximum = max(a[j], maximum)
            minimum = min(a[j], minimum)
            # print(j, minimum, maximum, dp[j-1])
            # print(dp)
            maximum_dp=max(maximum_dp, dp[j-1]+maximum-minimum)
            # print("max_dp", maximum_dp)
        # print(maximum_dp)
        dp[i] = maximum_dp
        # print(dp)
    


calc(a, 1, dp, n)
# print(a)
# print(dp)
# print(dp[-2])
for l, r, x in queries:
    # print("---"*3)
    for i in range(l-1, r):
        a[i]+=x
    # print(a)
    calc(a, l-1, dp, n)
    # print(dp)
    print(dp[-2])
    
