n, m = list(map(int, input().split()))
p = [input() for _ in range(n)]
met = [[False for _ in range(m)] for _ in range(n)]
groups = []
# print(groups)
for i in range(1, n-1):
    for j in range(1, m-1):
        if met[i][j]: continue
        if p[i][j]=="#": continue
        need_to_meet = [(i, j)]
        # print(i, j)
        k = 0
        while k < len(need_to_meet):
            if met[need_to_meet[k][0]][need_to_meet[k][1]]: 
                need_to_meet.pop()
                continue
            if p[need_to_meet[k][0]][need_to_meet[k][1]]=="#":
                met[need_to_meet[k][0]][need_to_meet[k][1]] = True
                need_to_meet.pop()
                continue
            print(k, need_to_meet[k][0], need_to_meet[k][1])
            met[need_to_meet[k][0]][need_to_meet[k][1]] = True
            need_to_meet.append((need_to_meet[k][0]+1, need_to_meet[k][1]))
            need_to_meet.append((need_to_meet[k][0]-1, need_to_meet[k][1]))
            need_to_meet.append((need_to_meet[k][0], need_to_meet[k][1]+1))
            need_to_meet.append((need_to_meet[k][0], need_to_meet[k][1]-1))
            k+=1
        groups.append(need_to_meet)
print([m for m in met])
print([group for group in groups])

