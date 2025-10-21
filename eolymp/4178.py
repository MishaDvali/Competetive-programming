n, w = map(int, input().split())
dp = [[0 for _ in range(w+1)] for _ in range(n+1)]
ps = [0 for _ in range(n + 1)]
ws = [0 for _ in range(n + 1)]
print(dp)
for i in range(1, n+1):
    a, b = tuple(map(int, input().split()))
    ps[i] = b
    ws[i] = a
for i in range(1, n+1):
    for j in range(min(w+1, ws[i])):
        dp[i][j] = dp[i-1][j]
    for j in range(ws[i], w+1):
        print(i, j)
        dp[i][j] = max(dp[i-1][j], dp[i-1][j-ws[i]] + ws[i])
backtrack = []

j = w
for i in range(n, 0, -1):
    if dp[i][j] != dp[i-1][j]:
        backtrack.append(i)
        j -= ws[i]
print(*reversed(backtrack))
    
