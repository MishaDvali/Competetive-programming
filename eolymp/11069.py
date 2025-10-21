w, b = [int(x) for x in input().split()]
#todo
n, m = 3, 250
more = max(w, b)
less = min(w, b)

if more > less * 3 + 1:
    print(-1)
else:
    diff = more - less
    if diff == 0 or diff == 1:
        n, m = 1, w+b
        print(n, m)
        if more == w:
            for i in range(w+b):
                if i % 2 == 0:
                    print('w', end='')
                else:
                    print('b', end ='')
        if more == b:
            for i in range(w+b):
                if i % 2 == 0:
                    print('b', end=' ')
                else:
                    print('w', end = ' ')

    placed_vert = diff -1
    placed_above = None
# print(f'{n} {m}')
# for i in range(n):
#     print('.' * m)
