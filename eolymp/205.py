s = input()
n = len(s)
def check_palindrome(s, n, i, j):
    # print(i, j)
    for k in range((j-i+1)//2):
        if s[i+k] != s[j-k]:
            return False
    return True
def solve(s, n):
    for slice_range in range(n, 1, -1):
        for start_palindrome in range(n-slice_range+1):
            if not check_palindrome(s, n, start_palindrome, start_palindrome+slice_range-1):
                return slice_range
    return 0
print(solve(s, n))


