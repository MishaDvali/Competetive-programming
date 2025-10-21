import sys

n_str = sys.stdin.readline()
n = int(n_str)
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

possible_a = set()
possible_b = set()
ans = None
for i in range(n-1, -1, -1):
    if a[i] + n - 1 - i in possible_b:
        ans = i+1
        break
    if b[i] + n - 1 - i in possible_a:
        ans = i+1
        break
    possible_a.add(a[i] + n - i - 1)
    possible_a.add(a[i] + n - i)
    possible_b.add(b[i] + n - i - 1)
    possible_b.add(b[i] + n - i)
print(ans-1)


# to do