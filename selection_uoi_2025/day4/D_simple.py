n, m = list(map(int, input().split()))
p = [input() for _ in range(n)]
ans = 0
for i in range(n):
    power = 0
    streak = False
    for j in range(m):
        if p[i][j]==".":
            if streak:
                continue 
            streak=True 
            power+=1
        if p[i][j]=="#":
            streak=False 
    ans+=2**power


