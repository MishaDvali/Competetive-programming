for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    i = 0
    is_possible=True
    while i < n and i < n:
        # print(ia, ib)
        if b[i] == a[i] or b[i] == a[i] + 1:
            i+=1
        else:
            is_possible=False
            break
    # print(ia, ib)
    if is_possible:
        print("YES")
    else:
        print("NO")




