n = int(input())
b = 0
ch = True
for _ in range(n):
    i = input().split()
    c = int(i[1])
    if i[0] == "spend":
        c = -c
    b += c
    if b < 0:
        ch=False
print("chinazes" if ch else "debt")