def pairs(n):
    count = 0
    m = int(n ** 0.5)
    for i in range(1, m + 1):
        if n % i == 0:
            count += 1
    return count

def smallest_number(k):
    n = 1
    while pairs(n) != k:
        n += 1
    return n

k = int(input())
print(smallest_number(k))

