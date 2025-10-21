from math import gcd
n, q = list(map(int, input().split()))
a = list(map(int, input().split()))
queries = [list(map(int, input().split())) for _ in range(q)]
cached = None #[[-1 for _ in range(n)] for i in range(n)]
def count_interesting(l, r, n, q, a, queries, cached):
    ans=0
    for i in range(l, r+1):
        # print(i, ans)
        # c_gcd = a[i]
        j=i
        while j<=r and gcd(*a[i:j+1])!=1:#gcd(c_gcd, a[j])!=1:
            j+=1
            ans+=1
    return ans

def change(x, v, n, q, a, queries, cached):
    a[x] = v
    pass

for query in queries:
    # print(query)
    # print(a)
    if query[0] == 1:
        change(query[1]-1, query[2], n, q, a, queries, cached)
    else:
        print(count_interesting(query[1]-1, query[2]-1, n, q, a, query, cached))


