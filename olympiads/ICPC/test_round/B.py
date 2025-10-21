
n = int(input())
# a = [None for _ in range(n)]
# numbers = [0 for _ in range(n)] 
# ilr = [None for _ in range(n)]
# for i in range(n):
#     l, r = tuple(map(int, input().split()))
#     ilr[i]= (i, l, r)
#     numbers[l+r] += 1
# for i, l, r in ilr:
#     a[i] = i + r
# for i in range(n-1):
#     print(a[i], end=" ")
# print(a[-1], end="")
a = [0 for _ in range(n)]
for i in range(n):
    a[i] = sum(map(int, input().split()))
for i in range(n-1):
    print(a[i], end=" ")
print(a[-1])