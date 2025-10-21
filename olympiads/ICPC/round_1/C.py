n = int(input())
a = list(map(int, input().split()))

ptypes = {}
one_pizza = 0
pizza_in_day = 0
days = 0
for i in range(n):
    
    if pizza_in_day == 0:
        ptypes[a[i]] = 1
        one_pizza+=1
        pizza_in_day+=1
        print(ptypes)
        continue
    if one_pizza == 0:
        ptypes={}
        pizza_in_day=0
        days+=1
        print(ptypes)
        continue
    if ptypes.get(a[i]) is not None:
        v = ptypes[a[i]]
        if v == 1:
            one_pizza-=1
            ptypes[a[i]]+=1
        pizza_in_day+=1
        if one_pizza == 0:
            ptypes={}
            pizza_in_day=0
            days+=1
        print(ptypes)
        continue
    else:
        ptypes[a[i]]=1
        pizza_in_day+=1
        one_pizza+=1
        print(ptypes)
print(days)