n, m = list(map(int, input().split()))
pic = [input() for _ in range(n)]
met = [[False for _ in range(m)] for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(m):
        # print(i, j, pic[i][j], met[i][j], end=";")
        if pic[i][j] == ".":
            continue
        if met[i][j] == True:
            continue
        met[i][j] = True
        # print(i, j)
        ans += 1
        k = 1
        while i + k < n and pic[i+k][j] == "*":
            met[i+k][j] = True
            k+=1
        l = 1
        while j + l < m and pic[i][j+l] == "*" :
            for o in range(k):
                met[i+o][j+l] = True
            l+=1
# [print(met[i]) for i in range(n)]
print(ans)

