n = int(input())
edges = [[] for _ in range(n)]
edges_status = [[] for _ in range(n)]
b = list(map(int, input().split()))
debug = False
for _ in range(n-1):
    n1, n2 = tuple(map(lambda x: int(x)-1, input().split())) 
    edges[n1].append(n2)
    edges[n2].append(n1)
    edges_status[n1].append(0)
    edges_status[n2].append(0)

visited=set()
to_visit = []
possible = True
c = [len(node_edges) for node_edges in edges]
for i in range(n):
    if c[i] < b[i]:
        possible=False
    if c[i] % 2 != b[i]%2:
        possible=False
# looking for leafs O(n)
for i in range(n):
    if len(edges[i]) == 1:
        to_visit.append(i) 

center = None 
for i in range(n):
    if len(edges[i]) > 1:
        center = i

if possible:
    print("YES")
    for i in range(n):
        if i == center:
            continue
        if b[i] == 1:
            print(i+1, center+1)
        else:
            print(center+1, i+1)
else:
    print("NO")