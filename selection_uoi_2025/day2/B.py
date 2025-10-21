n, k = list(map(int, input().split()))
politics = [[int(v)-1 for v in input().split()] for _ in range(n)]

def solve(n, k, politics):
    move = [[-1 for _ in range(n)] for _ in range(n)]
    fr = 0
    to = 1
    for hater_index in range(len(move[0])):
        if politics[0][hater_index] == 1:
            move[0][hater_index]=1

    move_number = 1

    while move[to][fr] == -1:
        move_number+=1
        if move_number==k:
            return to
        move[to][fr]=move_number
        temp_to=politics[to][fr]
        fr = to
        to = temp_to
    # [print("---") for _ in range(3)]
    # [print(move[i]) for i in range(n)]
    # [print("---") for _ in range(3)]
    move_number+=1
    cycle = move_number-move[to][fr]
    k-=move[to][fr]
    k = k % cycle
    for i in range(k):
        move[to][fr]=move_number
        temp_to=politics[to][fr]
        fr = to
        to = temp_to

    return to

if k == 1:
    print(1)
elif k == 2:
    print(2)
else:
    print(solve(n, k, politics)+1)

