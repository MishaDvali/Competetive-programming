cache = {}

def format(min_height, cubes):
    return min_height + cubes * 1000
def calc(min_height: int, cubes: int):
    if cubes == 0:
        return 1
    if min_height > cubes:
        return 0
    if min_height == cubes:
        return 1
    if min_height * 2 == cubes:
        return 1
    cached_val =  cache.get(format(min_height, cubes)) 
    if cached_val is not None:
        return cached_val
    s = 0
    for i in range(min_height, cubes + 1):
        c = calc(i + 1, cubes - i)
        # print(i)
        # print(f"new min height: {i}, variants: {c}, cubes: {cubes - i}, level: {rec}")
        s += c
    cache[format(min_height, cubes)] = s
    return s

# if calc(1, 1) != 1:
#     print("1 failed with: ", calc(1, 1))
# if calc(1, 2) != 1:
#     print("1 failed with: ", calc(1, 1))
# if calc(1, 3) != 3:
#     print("1 failed with: ", calc(1, 1))
cubes = int(input())
print(calc(min_height=1, cubes=cubes))
