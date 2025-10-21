from collections import defaultdict
for n_max in range(1, 1001):#_ in range(int(input())):
    # n_max =int(input())
    possible_n_dict = defaultdict(lambda: 0)
    for a in range(1, n_max+1):
        new_possible = 1
        for b in range(1, n_max+1):
            new_possible*=a
            possible_n_dict[new_possible] += 1
    possible_n = list(map(lambda p: p[1], sorted(list(possible_n_dict.items()), key=lambda p: p[0])))
    ss = [None for _ in range(len(possible_n))]
    last_ss = 0
    for i in range(len(possible_n)-1, -1, -1):
        last_ss+=possible_n[i]
        ss[i]=last_ss
    ans = 0
    for i in range(len(possible_n)):
        ans+=possible_n[i] * ss[i]
    print(n_max, ":", ans, ",")
