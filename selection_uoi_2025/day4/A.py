n = int(input())
to_left = []
to_right = []
for _ in range(n):
    i = input().split()
    if i[0] == "L":
        to_left.append(int(i[1]))
    elif i[0] == "G":
        to_right.append(int(i[1]))
# print(to_left, to_right)
to_left.sort()
to_right.sort(reverse=True)
def check_pos(p) -> int:
    ans=0
    for left in to_left:
        if p <= left:
            ans+=1
        else:
            # break
            pass
    for right in to_right:
        if p >= right:
            ans+=1
        else:
            # break
            pass
    return ans

m = 0
for i in to_left+to_right:
    # print(i, check_pos(i))
    m = max(m, check_pos(i))
print(n-m)


