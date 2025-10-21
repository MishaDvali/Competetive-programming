# example below, replace it with your solution
n = int(input())
r = input()
prefix_sum = [0 for _ in range(n)] 
same = [0 for _ in range(2*n+2)]
prefix_sum[0] = 1 if r[0] == "a" else -1
same[0] = 1 
same[prefix_sum[0]] = 1
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i-1]
    prefix_sum[i] += 1 if r[i] == "a" else -1
    same[prefix_sum[i]]+= 1
ans = 0
for i in range(2*n+2):
    x = same[i]
    ans += (x*x) - ((x+1)*x/2)
print(int(ans))
'''
   a  b  a  a  a  b  b
0  1  0  1  2  3  2  1

x
1 2 
1 3 
1 4
...
1 x
2 3
2 4
...
2 x
=
(x - 1) + (x - 2) + (x - 3) + ... + (x-x)
                            x
x * x - (1 + 2 + 3 +...+ x)
x * x - ((x+1)*(x)/2)
'''

