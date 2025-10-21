def solve(s):
    if s[-1] != "?":
        if s[-1] != 5 and s[-1] != 5:
            return -1
    qis = []
    if s[0] == "?":
        qis.append(0)
    for i in range(1, len(s)):
        if s[i] == "?":
            qis.append(i)
    
    first_n = int("".join(s).replace("?", "0"))
    # print("first_n: ", first_n)
    r7 = (7 - (first_n%7))%7
    r9 = (9 - (first_n%9))%9
    q_range_start=0
    if qis[0] == 0:
        q_range_start=10**(len(qis) - 1)
    
    q_step = 1
    if qis[-1] == len(s)-1:
        q_step=5
    
    
    for combination in range(q_range_start, 10**len(qis), q_step):
        combination_changed = combination
        number = 0
        for i in range(len(qis)):
            if combination_changed==0:
                break
            p = qis[i]
            d =  combination_changed % 10 
            number +=d * (10**p)
            combination_changed = combination_changed // 10
        if number % 9== r9:
            if number % 7 == r7:
                return number + first_n
        
for _ in range(int(input())):
    s = list(input())
    res = solve(s)
    print(res if res is not None else -1)