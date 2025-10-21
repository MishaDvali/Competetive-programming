n, k = map(int, input().split())
toKill = k-1
a = []
for i in range(1, n + 1):
    a.append(i)

for i in range(n-1):
    a.pop(toKill)
    toKill = (toKill + k -1) % len(a)

print(a[0])
