amount = int(input())
a = list(map(int, input().split()))
is_good = [2 for _ in range(1000)]
is_good[0] = 0
is_good[1] = 1

for i in range(2, 1000):
    # print("i:", i)
    if is_good[i] == 1 or is_good[i]==0:
        continue
    n = i
    met = set()
    while is_good[n] == 2 and n not in met:
        met.add(n)
        n = sum([int(c)*int(c) for c in str(n)])
        # print(n)
    should_assign = 0 if is_good[n]==2 or is_good[n] == 0 else 1
    # print("Should assign: ", should_assign)
    for m in met:
        is_good[m] = should_assign


# print(is_good)

for element in a:
    nex = sum([int(c)**2 for c in str(element)])
    print(is_good[nex], end="")


