import sys


def ask(i, j, k):
    sys.stdout.write(f"? {i} {j} {k}\n")
    sys.stdout.flush()
    res = int(sys.stdin.readline())
    if res == -1:
        exit(0)
    return res


def answer(i, j):
    sys.stdout.write(f"! {i} {j}\n")
    sys.stdout.flush()


n = int(sys.stdin.readline())

x1 = 1
x2 = 2
for i in range(3, n+1):
    if ask(x1, x2, i):
        continue
    if ask(x1, i, x2):
        x2 = i
    else:
        x1 = i 
answer(x1, x2)