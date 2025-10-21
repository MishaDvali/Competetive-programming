n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
is_snake_array = [False for _ in range(n)]
for b_element in b:
    is_snake_array[b_element] = True
s_left = [len(edges[i]) for i in b]
tree = [[] for _ in range(n)]
for _ in range(n-1):
    u, v = tuple(map(int, input().split()))
    tree[u].append(v)
    tree[v].append(u)
to_visit = []
for i in range(n):
    if len(tree[i]) == 0:
        to_visit.append(e)
i = 0
visited=set()
while i<len(to_visit):
    node = to_visit[i]
    if node in visited:
        continue
    edges = tree[i]
    is_snake = is_snake_array[i]
    if is_snake:
        if s_left[i] > 1:
            to_visit.append(i)
        else:
            visited.add(node)
            pass #TODO to figure out a leaf that is above and to add to the array

            
    


