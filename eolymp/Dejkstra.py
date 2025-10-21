import enum
from typing import List
infinity = 10000


amount_of_vertices = int(input())

matrix: List[List[int]] = []
for i in range(amount_of_vertices):
    matrix.append(list(map(int, input().split(" "))))

need_to_check = [0]
distances = [10000 for _ in range(amount_of_vertices)]
distances[0] = 0
i = 0
while i < len(need_to_check):
    src = need_to_check[i]
    for destination, distance in enumerate(matrix[src]):
        if distance == infinity or distance == 0:
            continue
        if distances[src] + distance < distances[destination]:
            need_to_check.append(destination)
            distances[destination] = distances[src] + distance
    i += 1 

for i, dist in enumerate(distances):
    print(f"Vertice {i + 1}: {dist} ")


