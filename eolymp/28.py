import random
def calc(a, b):
    prod = 1
    for i in range(a, b +1):
        prod*=i
    return int(prod)

def solve(target):
    leftp = 2
    rightp = 2
    prod = 2
    while True:
        # if prod != calc(leftp, rightp):
        #     print("prod is wrong", leftp, rightp, prod, calc(leftp, rightp))
        #     return

        if prod == target:
            return leftp, rightp
        if prod < target:
            rightp += 1
            # prod *= rightp
        else:
            # prod = int(prod / leftp)
            leftp += 1
        prod = calc(leftp, rightp)
        # if leftp == a and rightp == b:
            # print("Exceed: ", leftp, rightp, "\n", calc(leftp, rightp), "\n", int(prod))
            # return
target = int(input())
solved = solve(target)
print(solved[0], solved[1])

# for i in range(100):
#     print()
#     print(i)
#     a = random.randint(2, 200)
#     b = random.randint(a, a + 200)
#     prod = calc(a, b)
#     solved =  solve(prod, a, b)
#     if not (a, b) == solved:
#         print("The anser is wrong: ", a, b, prod, solved)
#

