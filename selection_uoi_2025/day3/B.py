ans = 0
# from random import randint

n, k = list(map(int, input().split()))
houses = [list(map(int, input().split())) for _ in range(n)]
# n = 50
# k = 100000
# houses =[[i, randint(1, 100)] for i in range(n)]
dp = [dict() for _ in range(n)]
s = [0 for _ in range(n)]
s[n-1]=houses[n-1][1]
for i in range(n-2, -1, -1):
    s[i] = s[i+1] + houses[i][1]
for i in range(0, n):
    dp[i][min(k, houses[i][1])] = 1
    house = houses[i]
    g = house[1]
    h = house[0]
    dp[i][min(k, g)] = 1
    for j in range(i-1, -1, -1):
        if houses[j][0] <= h:
            for coins, amount in dp[j].items():
                if coins + g < k-s[i]:
                    continue
                if dp[i].get(min(k, coins+g)) is None:
                    dp[i][min(k, coins+g)] =0
                dp[i][min(k, coins + g)]+=amount
    for coins, amount in dp[i].items():
        if coins >=k:
            ans+=amount
# [print(dict(o)) for o in dp]
print(ans)
