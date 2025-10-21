from typing import List, Tuple
from collections import deque


tedges =List[List[List[int]]]
tto_pair: List[List[int]]

n, m = list(map(int, input().split()))

edges:tedges = [[] for _  in range(n)]
for i in range(n-1):
    a, b = tuple(map(int, input().split()))
    edges[a].append([b, i])
    edges[b].append([a, i])

to_pair: List[Tuple[int, int]] = []
for _ in range(m):
    to_pair.append(tuple(map(int, input().split())))


def find_path(a_n, b_n, edges):
    pass
    

def mark_path(a_n, b_n, edges, n):
    pass 

def mark_all_path(n, m, edges, to_pair) -> None:
    for i in range(len(to_pair)):
        mark_path(to_pair[i][0], to_pair[i][1], edges, i)

def check_node(node_n, edges):
    pass


def solve():
    mark_all_path(n, m, edges, to_pair)

     

