rows, columns = tuple(map(int, input().split()))
coins = [list(map(int, input().split())) for _ in range(rows)]
dp = [[None for _ in range(columns)] for _ in range(rows)]
dp[-1][0] = coins[-1][0]
for i in range(1, columns):
    dp[-1][i] = dp[-1][i-1] + coins[-1][i]
for i in range(rows-2, -1, -1):
    for j in range(columns):
        if j == 0:
            dp[i][j] = dp[i+1][j] + coins[i][j]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i][j-1]) + coins[i][j]
reversed_back_track = ""
y = 0
x = columns-1
while True:
    if x == 0 and y== rows-1:
        break
    if y == rows-1:
        reversed_back_track += "R"
        x-=1
    elif x == 0:
        reversed_back_track += "F"
        y+=1
    elif dp[y][x] - coins[y][x] == dp[y+1][x]:
        reversed_back_track += "F"
        y+=1
    else:
        reversed_back_track += "R"
        x-=1
# print(dp)
print(reversed_back_track[::-1])