from typing import List, Union

world: List[List[List[Union[str, None, int]]]] = []

height, width, src_y, src_x, dest_y, dest_x = tuple(map(int, input().split()))
src_x -= 1
src_y -= 1
dest_x -= 1
dest_y -= 1
for i in range(height):
    world.append([])
    for char in input():
        world[i].append([char, None, -2])
# world[src_y][src_x][2] = 0

need_to_check_now = set([(src_x, src_y)])
will_need_to_check = set()
will_will_need_to_check = set()

def explore(x, y, iteration) -> None:
    # print(f"x:{x} y:{y} i:{iteration}")
    cell = world[y][x]
    if cell[2] != -2:
        return
    cell[2] = iteration
    for new_x, new_y in [(x - 1, y), (x+1, y), (x, y+1), (x, y-1)]:
        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
            continue
        if world[new_y][new_x][0] == "#":
            continue
        if world[new_y][new_x][2] != -2:
            continue
        # print(f"new_x:{new_x} new_y:{new_y}")
        if world[new_y][new_x][0] == ".":
            will_need_to_check.add((new_x, new_y))
            continue
        if world[new_y][new_x][0] == "W":
            will_will_need_to_check.add((new_x, new_y))
            continue
        print("NO")
        
        
i = 0
should_break = False
while True:
    if len(need_to_check_now) == 0 and len(will_need_to_check) == 0:
        break

    # for line in world:
    #     print(list(map(lambda o: o[2], line)))
    # print()
    for src_x, src_y in need_to_check_now:
        explore(src_x, src_y, i)
        if src_x == dest_x and src_y == dest_y:
            should_break = True
            break
    if should_break:
        # for line in world:
        #     print(list(map(lambda o: o[2], line)))
        break

    i += 1
    need_to_check_now = will_need_to_check
    will_need_to_check = will_will_need_to_check
    will_will_need_to_check = set()

def trace_back(x, y):
    cell = world[y][x]
    if cell[2] == 0:
        return ""
    shortest_path = cell[2]
    for new_x, new_y, direction in [(x - 1, y, "E"), (x+1, y, "W"), (x, y+1, "N"), (x, y-1, "S")]:
        if new_x < 0 or new_x >= width or new_y < 0 or new_y >= height:
            continue
        diff = shortest_path -  world[new_y][new_x][2] 
        # print(world[new_y][new_x])
        # print(shortest_path, world[new_y][new_x][2], diff)
        # print(new_x, new_y)
        if diff == 2 and cell[0] == "W":
            return trace_back(new_x, new_y) + direction
        if diff == 1 and cell[0] ==".":
            return trace_back(new_x, new_y) + direction

    # print(x, y)
    # print(cell[2])
    raise Exception("Impossible")

print(trace_back(dest_x, dest_y))
