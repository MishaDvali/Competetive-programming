s = list(input())
s.sort()
def next(s, n):
    pivot_point = None
    for i in range(n-2, -1, -1):
        if ord(s[i]) < ord(s[i+1]):
            pivot_point=i 
            break
    # print(pivot_point)
    if pivot_point is None:
        return None
    to_swap_with = n-1
    for i in range(pivot_point+1, n-1):
        if ord(s[i+1]) < ord(s[pivot_point]):
            to_swap_with = i
            break
    s[pivot_point], s[to_swap_with] = s[to_swap_with], s[pivot_point]
    for shift in range((n-pivot_point-1)//2):
        s[pivot_point+1+shift], s[n-shift-1] = s[n-shift-1], s[pivot_point+1+shift]
    return s
n = len(s)
while s is not None:
    print("".join(s))
    s = next(s, n)
