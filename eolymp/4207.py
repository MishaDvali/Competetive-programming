from collections import Counter
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

def check(a, b):
    an = Counter(str(a))
    bn = Counter(str(b))
    # print(an, bn)
    z = 0
    for k, v in an.items():
        if bn.get(k) is None: continue
        z +=min(v, bn[k])
    y = 0
    for i in range(6):
        if a // (10^i) == b // (10^i):
            y +=1
    return y, z-y 
        

def solve(n, data):
    have_found = False
    for i in range(100000, 1000000):
        #if i == 111111:
            #print(check(i, x))
        failed=False
        for x, y, z in data:
            if (y, z) == check(i, x):
                if have_found == True:
                    print("NO")
                    return
            else:
                failed=True
                break
        if not failed:
            have_found=True
    if have_found:
        print("YES")
    else:
        print("NO")

solve(n, data)
            