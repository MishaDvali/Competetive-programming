n = int(input())
cache = [0 for i in range(n + 2)]
def find(stair_number):
    if stair_number == 1:
        return 1
    if stair_number == 2:
        return 2
    if stair_number == 3:
        return 4
    if cache[stair_number] != 0:
        return cache[stair_number]
    a = find(stair_number - 1) + find(stair_number - 2) + find(stair_number - 3)
    cache[stair_number] = a
    return a
print(find(n))
for i in range(2, 61):
    print(i)
    cache = [0 for j in range(i + 2)]
    print(find(i))
