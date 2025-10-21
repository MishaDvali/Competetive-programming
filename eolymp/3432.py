from collections import defaultdict
from typing import Dict, List, Set, Tuple, Union

def solve(amount_of_roads: int, amount_of_LPG: int, volume: int):
    volume *= 10
    src, final_dest = input().split()
    cities: Dict[str, List[Union[List[Tuple[str, int]], bool, int]]] = defaultdict(lambda: [[], False, 99999])
    for i in range(amount_of_roads):
        data = input().split()
        road_length = int(data[2])
        cities[data[0]][0].append((data[1], road_length))
        cities[data[1]][0].append((data[0], road_length))

    for i in range(amount_of_LPG):
        city = input()
        cities[city][1] = True

    i = 0
    need_to_check = [cities[src]]

    def explore(city: List[Union[List[Tuple[str, int]], bool, int]], volume_left: int) -> None:
        for dest_name, distance in city[0]:
            if distance > volume_left:
                continue
            if city[1]:
                dest_city = cities[dest_name]
                if dest_city[2] > city[2] + distance:
                    dest_city[2] = city[2] + distance
                    print(dest_city[2])
                    need_to_check.append(dest_city)
                continue
            explore(cities[dest_name], volume_left - distance)

    while i < len(need_to_check):
        city = need_to_check[i]
        explore(city, volume)
        i += 1

    if cities[final_dest][2] == 99999:
        print(cities)
        print(-1)
    else:
        print(cities)
        print(cities[final_dest][2])


while True:
    amount_of_roads, amount_of_LPG, volume = tuple(map(int, input().split()))
    if amount_of_roads == 0 and amount_of_LPG == 0 and volume == 0:
        break
    solve(amount_of_roads, amount_of_LPG, volume)


