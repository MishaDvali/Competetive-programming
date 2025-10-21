'''
W -> CO
O -> CW

CO -> W  {1, 1, 0} -> {0, 0, 1}
CW-> O 
OW -> C

cow -> CC -> - {1, 1, 1} -> {0}
WCW -> WO -> C  {2, 1, 0} -> {1, 0, 1} -> {0, 1, 0}
WWW -> W {3, 0, 0} -> {1, 0, 0}

WCOW -> {1, 1, 2} -> {0, 0, 1} 
'''
ord_w = ord("W")
ord_o = ord("O")
ord_c = ord("C")
letters=[ord_w, ord_o, ord_c]
s = input()
# s = ''.join(["C"*2000]+["O"*2000]+["W"*2000])
q = int(input())
queries = [tuple(map(lambda i: int(i)-1, input().split())) for _ in range(q)]

counters = [[0 for _ in range(90)] for _ in range((len(s) // 1000)+1)]

for j in range((len(s)//1000)+1):
    counter = counters[j]
    for i in range(j*1000, min(len(s), (j*1000)+1000)):
        counter[ord(s[i])]+=1
# print(counters)
# for c in counters:
#     print(c[ord_c])
#     print(c[ord_o])
#     print(c[ord_w])
def count(l, r, c, cache):
    amount_of_cached = (r+1-l) // 1000
    if not cache or amount_of_cached==0:
        for i in range(l, r+1):
            c[ord(s[i])]+=1
        return 


    cached_left = ((l+999)//1000)*1000
    cached_right = (((r+1)//1000)*1000)-1
    if l %1000!=0:
        count(l, cached_left-1, c, False)
    if (r + 1)%1000!=0:
        count(cached_right+1, r, c, False)
    
    if amount_of_cached!=0:
        for i in range(cached_left//1000, (cached_right +1)//1000):
            c[ord_c] += counters[i][ord_c]
            c[ord_o] += counters[i][ord_o]
            c[ord_w] += counters[i][ord_w]


c = [0 for _ in range(90)]
# count(0, 2, c, True)
# print(c[ord_c], c[ord_o], c[ord_w])
# c[ord_c]=0
# c[ord_w]=0
# c[ord_o]=0
# count(0, 3999, c, True)
# print(c[ord_c], c[ord_o], c[ord_w])
# c[ord_c]=0
# c[ord_w]=0
# c[ord_o]=0
# count(2000, 5999, c, True)
# print(c[ord_c], c[ord_o], c[ord_w])
# c[ord_c]=0
# c[ord_w]=0
# c[ord_o]=0
# count(4629, 5291, c, True)
# print(c[ord_c], c[ord_o], c[ord_w])
# c[ord_c]=0
# c[ord_w]=0
# c[ord_o]=0
# count(500, 3999, c, True)
# print(c[ord_c], c[ord_o], c[ord_w])
# c[ord_c]=0
# c[ord_w]=0
# c[ord_o]=0
# count(500, 4500, c, True)
# print(c[ord_c], c[ord_o], c[ord_w])
# c[ord_c]=0
# c[ord_w]=0
# c[ord_o]=0

for query in queries:
    c[ord_c]=0
    c[ord_w]=0
    c[ord_o]=0
    count(query[0], query[1], c, True)
    # print()
    # print()
    # print(s[query[0]:query[1]+1])
    # print(c)
    m = min(c[ord_w], c[ord_o], c[ord_c])
    for l in letters:
        c[l] -= m
    for l in letters:
        c[l] = c[l]%2

    sum_of_values = c[ord_c] + c[ord_o] + c[ord_w]
    if sum_of_values==0:
        print("N", end="")
        continue
    if sum_of_values==1:
        have_found = False
        for l in letters:
            if c[l]==1:
                if l==ord_c: 
                    print("Y", end="") 
                    have_found=True
        if not have_found: print("N", end="")
    if sum_of_values==2:
        have_found = False
        for l in letters:
            if c[l]==0:
                if l==ord_c: 
                    print("Y", end="") 
                    have_found=True
        if not have_found: print("N", end="")
    pass



