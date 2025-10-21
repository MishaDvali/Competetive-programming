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
if debug:
    print("To_visit: ", list(map(lambda x: x +1, to_visit)))
i = 0

while i < len(to_visit) and possible:
    node = to_visit[i]
    if node in visited:
        i+=1
        continue
    if c[node] == 0:
        if b[node] != 0:
            possible=False
        break            
    if c[node] > 1 or c[node] < 1:
        i+=1
        continue
    if debug:
        print(f"""
        node: {node+1}
        to_visit: {list(map(lambda x: x +1, to_visit))}
        b: {b}
        c: {c}
        """)
    visited.add(node)
    unstatus_edge_i = None
    unstatus_node = None

    for j in range(len(edges[node])):
        next_node = edges[node][j]
        edge_status = edges_status[node][j]
        if edge_status == 0: 
            unstatus_node = next_node
            unstatus_edge_i = j
            # print("unstatus node:", unstatus_node)

    
    if b[node] == 1:
        if unstatus_node not in visited:
            to_visit.append(unstatus_node)
        edges_status[node][unstatus_edge_i] = 1
        edges_status[unstatus_node][edges[unstatus_node].index(node)] = -1
        b[node] -=1
        b[unstatus_node] +=1
        c[node] -=1
        c[unstatus_node]-=1
    elif b[node] == -1:
        edges_status[node][unstatus_edge_i] = -1
        edges_status[unstatus_node][edges[unstatus_node].index(node)] = 1
        b[node] +=1
        b[unstatus_node] -=1
        c[node] -=1
        c[unstatus_node]-=1
        if unstatus_node not in visited:
            to_visit.append(unstatus_node)
    else:
        possible=False
        break

    i +=1

if not possible:
    print("NO")
else:
    print("YES")
    if debug:
        print(edges_status)
    for i in range(n):
        for j in range(len(edges[i])):
            if edges_status[i][j] == 1:
                print(i+1, edges[i][j]+1)





