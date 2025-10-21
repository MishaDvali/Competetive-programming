
for _ in range(int(input())):
    x1, y1, x2, y2 = tuple(map(int, input().split()))
    if x1 < 0:
        x1=-x1
        x2=-x2
    if y1<0:
        y1=-y1
        y2=-y2
    
    if x1 - x2 != y1 - y2:
        print("YES")
        continue
    if x1 < x2:
        print("YES")
        continue
    if ((x1 > 0 and x2 > 0) or (x1<0 and x2<0)) and ((y1 > 0 and y2 > 0) or (y1<0 and y2<0)):
        print("NO")
        continue
    print("YES")
    continue

    