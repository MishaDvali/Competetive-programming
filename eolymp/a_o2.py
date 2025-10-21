import sympy
import math

k = int(input())

def ans(n):
    prods = {1}
    divisors = sympy.factorint(n)

    for divisor, exponent in divisors.items():
        new_prods = set()
        for new_exponent in range(exponent + 1):
            for prod in prods:
                new_prods.add(prod * (divisor ** new_exponent))
        prods = new_prods
    ans = len(prods) / 2
    root =  math.sqrt (n)
    if math.floor(root) == root and root in prods:
        ans += 1
    print(prods)
    return ans

should_iterate = False 

if k == 1:
    print(1)
if k == 2:
    print(4)
else:
    should_iterate = True

i = 3
while should_iterate:
    print(i)
    if ans(i) == k:
        print(i)
        break
    # if i > 1000:
    #     print("STOP")
    #     break
    i+=1


