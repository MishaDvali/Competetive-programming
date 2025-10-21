m, n = tuple(map(int, input().split()))
bm, bn = format(m, '064b'), format(n, '064b')
if n-m + 1< 3:
    print(2)
    print(m, n)
else:
    shared_one = len(bm)-1
    for i in range(len(bm)):
        if bm[i] =="1" and bn[i] == "1":
            shared_one = i
            break
    k = 0
    a = []
    for i in range(m, n+1):
        if format(i, '064b')[shared_one] == "1":
            k+=1
            a.append(i)
    print(k)
    print(*a)

        