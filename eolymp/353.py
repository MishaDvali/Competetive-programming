sweets = list(map(int, input().split(" ")))

a = sweets[0]
b = a
c = b
d = c
ai = 0
bi = 0
ci = 0
di = 0

for i in range(len(sweets) - 1):
    sweets[i] = sweets[i] + sweets[i + 1]
    s = sweets[i]
    if s > d:
        if s > c:
            if s > b:
                if s > a:
                    d = c
                    di = ci
                    c = b
                    ci = bi
                    b = a
                    bi = ai
                    a = s
                    ai = i 
                else:
                    d = c
                    di = ci
                    c = b
                    ci = bi
                    b = s 
                    bi = i 
            else:
                d = c
                di = ci
                c = s 
                ci = i 
        else:
            d = s
            di = i

s = a + b

assert a == max(sweets)
assert ai != bi
assert ai != ci
assert ai != di
assert bi != ci
#assert bi != di
#assert ci != di
if (di == bi):
    s = b + c
elif (ai - 1 == bi) or (ai + 1 == bi):
    if (ai - 1 == ci) or (ai + 1 == ci):
        s = max(a + d, b + c)
    else:
        s = a + c



print(s)
