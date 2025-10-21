input()
coins = list(map(int, input().split()))
ans = [0, coins[1], coins[2]]
for i in range(2, len(coins)):
    ans[i] = max(ans[i-2], ans[i-3]) + coins[i]
print(max(ans[-2], ans[-3]))
