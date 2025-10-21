
# from random import randint
n, m = list(map(int, input().split()))

edges = [[] for _  in range(n)]
for i in range(n-1):
    a, b = tuple(map(lambda o: int(o)-1, input().split()))
    edges[a].append([b, i])
    edges[b].append([a, i])
# [input() for _ in range(n-1)]
to_pair = sorted([sorted(list(map(lambda o: int(o)-1, input().split()))) for _ in range(m)], key=lambda o: o[0])
# to_pair = sorted([sorted([randint(0, n), randint(0, n)]) for _ in range(m)], key=lambda o: o[0])
# print(to_pair)



# print(to_pair)
def unite(to_pair):
    new_to_pair = []
    i = 0
    start = to_pair[0][0]
    end = to_pair[0][1]

    while i < len(to_pair)-1:
        if to_pair[i+1][0] < end:
            end = max(end, to_pair[i+1][1])
            i+=1
            continue 
        new_to_pair.append([start, end])
        start = to_pair[i+1][0]
        end = max(to_pair[i+1][1], end)
        i+=1
    new_to_pair.append([start, end])
    return new_to_pair

to_pair = unite(to_pair)
# print(to_pair)

# print(to_pair)
i = 0
range_index =0
ans = 1
while range_index < len(to_pair):
    # print(i, ans)
    # i - - s _ _ _ e - - -
    ans *= 2**(to_pair[range_index][0]-i)
    i = to_pair[range_index][0]

    # print(i, ans)
    # - - - i _ _ _ e - - -
    ans*=2
    i=to_pair[range_index][1]
    range_index+=1
    continue
ans *= 2**(n-i-1)
# print(ans)
print(int(ans%(10**9+7)))





        




