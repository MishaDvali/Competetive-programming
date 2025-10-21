n, m = tuple(map(int, input().split()))
t =[input() for _ in range(n)]
to_print=[]
def output(x1, x2, y1, y2, c):
    to_print.append([x1+1, x2+1, y1+1, y2+1, c])
for trio in range(0, n - (n%3), 3):
    # print(f"Trio: {trio+1} {trio+2} {trio+3}")
    first_row = t[trio]
    second_row = t[trio+1]
    third_row = t[trio+2]
    last=[]
    for i in range(m):
        if first_row[i] == "1" and second_row[i]=="0" and third_row[i]=="1":
            output(trio, trio+2, i, i, 1)
        else:
            last.append(i)
    output(trio+1, trio+1, 0, m-1, 0)
    for i in last:
        r1 = first_row[i] == "1"
        r2 = second_row[i] == "1"
        r3 = third_row[i] == "1"
        if r1 and r2 and r3:
            output(trio, trio+2, i, i, 1)
        elif r1 and r2:
            output(trio, trio+1,  i, i, 1)
        elif r2 and r3:
            output(trio+1, trio+2, i, i, 1)
        elif r1:
            output(trio, trio, i, i, 1)
        elif r2:
            output(trio+1, trio+1, i, i, 1)
        elif r3:
            output(trio+2, trio+2, i, i, 1)
print(len(to_print))
for e in to_print:
    print(*e)