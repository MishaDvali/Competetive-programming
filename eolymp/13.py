a, b, c= tuple(map(int, input().split()))
x1, y1, x2, y2, z2 = tuple(map(int, input().split()))
def dist(x1, x2, y1, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
def solve():
    if x2 != 0 and y2 !=0:
        return dist(x2, x1, y2, y1)
    if x2 == 0:
        if y2 == 0:
            return dist(x2, x1, y1, y2-b)
        else:
            return dist(x2, x1, y1, y2+b)
    if y2 == 0:
        if x2 == 0:
            return dist(y2, y1, x1, x2-a)
        else:
            return dist(y2, y1, x1, x2+a)


print(solve())
