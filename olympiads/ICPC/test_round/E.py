n = int(input())
ps = sorted([tuple(map(int, [i] + input().split())) for i in range(1, 3*n+1)], key=lambda p:p[1]*(10**10) + p[2])
t = [None for _ in range(n)]
for i in range(0, n*3, 3):
    t[i//3] = [ps[i][0], ps[i+1][0], ps[i+2][0]]
# print(ps)
for e in t:
    print(*sorted(e))
