n = int(input().split(" ")[0])
cache = [-1 for i in range(n + 1)]
broken = input().split(" ")
for s in range(len(broken)):
    broken[s] = int(broken[s])
    cache[broken[s]] = 0
def find(stair_number):
    global cache
    if stair_number == 1:
        if cache[1] != 0:
            return 1
        else:
            return 0
    if stair_number == 2:
        if cache[2] != 0:
            return 2
        else:
            return 0
    if stair_number == 3:
        if cache[3] != 0:
            return 4
        else:
            return 0
    if cache[stair_number] != -1:
        return cache[stair_number]

    n1 = find(stair_number - 1) 
    n2 = find(stair_number - 2) 
    n3 = find(stair_number - 3)
    a = n1 + n2 + n3
    print(cache)
    cache[stair_number] = a
    return a
print(cache)
print(find(n))
