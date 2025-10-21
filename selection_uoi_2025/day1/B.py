from collections import Counter
n =int(input())
cows = [int(cow)-1 for cow in input().split()]
pars = [[] for _ in range(n)]

def solve(n, cows, pars):
    for cow_index in range(n):
        pars[cows[cow_index]].append(cow_index)
    for par in pars:
        par.append(n)
        par.append(-1)
    # print(pars)
    ans = 0
    for l_cow_index in range(n-1):
        # print(f"l: {l_cow_index}")
        par_of_the_l_cow = cows[l_cow_index]
        max_r = pars[par_of_the_l_cow][pars[par_of_the_l_cow].index(l_cow_index)+1]
        for r_cow_index in range(l_cow_index+1, max_r):
            # print(f"r: {r_cow_index}")
            par_of_the_r_cow = cows[r_cow_index]
            if pars[par_of_the_r_cow][pars[par_of_the_r_cow].index(r_cow_index)-1] < l_cow_index:
                ans+=1
        # print(f"l_cow_index: {l_cow_index}, max_length: {max_r}, add: {max_r-l_cow_index-1}")
    return ans


counter = Counter(cows)
keys = counter.keys()
if len(keys)==n:
    print((n-1)*n//2)
elif len(keys)==1:
    print(0)
elif len(keys)==2:
    ans = 0
    for cow_index in range(n-1):
        if cows[cow_index] != cows[cow_index+1]:
            ans+=1
    print(ans)
else:
    print(solve(n, cows, pars))





