n, m, k = tuple(map(int, input().split()))
us = {}
ans = 0
rs = set()
for i in range(1, n+1):
    t, r, u = input().split()
    if r not in rs:
        ans+=1
        # print("r:", t, r, u)
        rs.add(r)
        us[u]=1
        continue
    if i <= m:
        ua = us.get(u)
        if ua is None:
            us[u]=1
        else:
            us[u]+=1
        if us[u] > k:
            continue
        # print("t:", t, r, u)
        ans+=1
        
print(ans)


