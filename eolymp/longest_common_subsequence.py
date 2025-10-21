# from collections import defaultdict
# from typing import DefaultDict
#
#
# table = {}
#
# def findMaxSubsequence(a, b):
#     cached = table.get(f"{a}-{b}")
#     if cached is not None:
#         return cached
#     if len(a) == 0:
#         return 0
#     if len(b)==0:
#         return 0
#     if a[0] == b[0]:
#         return findMaxSubsequence(a[1::], b[1::]) + 1
#     max_s = max(findMaxSubsequence(a[1::], b), findMaxSubsequence(a, b[1::]))
#     table.get(f"{a}-{b}")
#     return max_s
#
#
# while True:
#     a = input().split(" ")
#     b = input().split(" ")
#     print(findMaxSubsequence(a, b))

# table = {}
#
# def findMaxSubsequence(a, b):
#     cached =table.get(f"{a} {b}")
#     if cached is not None:
#         # print(f"Read cache {cached} for {a} and {b}")
#         return cached
#     if len(a) == 0 or len(b) == 0:
#         return 0
#     if a[0] == b[0]:
#         print(f"first character matched {a}, {b}")
#         c = findMaxSubsequence(a[1:], b[1:])
#         table[f"{a} {b}"] = c
#         return c + 1
#     c = findMaxSubsequence(a[1:], b)
#     d = findMaxSubsequence(a, b[1:])
#     if c > d:
#         m = c
#     else:
#         m = d
#     print(f"For strings {a} and {b} the max is {c}")
#     table[f"{a} {b}"] = m
#     return m
#
# _ = input()
# a = input().split(" ")
# _ = input()
# b = input().split(" ")
# print(findMaxSubsequence(a, b))


def longestCommonSubsequence(a, b):
        n = len(a)
        m = len(b)
        dpGrid = [[0] * (m + 1) for _ in range(n + 1)]

        for row in range(n - 1, -1, -1):
            for col in range(m - 1, -1, -1):
                if a[row] == b[col]:
                    dpGrid[row][col] = 1 + dpGrid[row + 1][col + 1]
                else:
                    dpGrid[row][col] = max(dpGrid[row + 1][col], dpGrid[row][col + 1])

        return dpGrid[0][0]

_ = input()
a = input().split(" ")
_ = input()
b = input().split(" ")
print(longestCommonSubsequence(a, b))
