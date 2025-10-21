
n, k = list(map(int, input().split()))
cities = input()
# print(cities)


cities = list(map(lambda o: 1 if o =="H" else -1, cities))
dp = [-1 for _ in range(n)]
dp.append(0)
def calc_dp(city_index: int, k: int, dp, cities):
    if city_index == 0:
        return  0 if cities[city_index] == 1 else 1
    if city_index == 1:
        if k == 1:
            return dp[0] if cities[city_index]==1 else dp[0]+1
        if dp[0]==0:
            return 1 if cities[city_index] == -1 else 0
        return 1


    total = 0
    best_dp = float('inf')
    for i in range(city_index, city_index - min(k-1, city_index) -1, -1):
        total += cities[i]
        best_dp=min(best_dp, dp[i-1] +1 if total <= 0 else dp[i-1])
        # print(f"i: {i}, best_dp: {best_dp}, total: {total}")
    return best_dp



def solve(dp, k, cities):
    for city_index in range(n):
        # print(f"city: {city_index}")
        dp[city_index] = calc_dp(city_index, k, dp, cities)
    # print(dp)
    return dp[-2]

if n == 1:
    if cities[0] == "H":
        print(0)
    else:
        print(1)
else:
    print( solve(dp, k, cities))



# for n, k, cities, ans in [
#         [3, 3, "GGG", 1],
#         [3, 3, "GHH", 0],
#         [3, 3, "HHH", 0],
#         [3, 3, "GHG", 1],
#         [3, 2, "HGH", 1],
#         [3, 2, "HHG", 1],
#         [7, 2, "HHHHHHH", 0],
#         [7, 7, "GGGGGGG", 1],
#         [7, 1, "GGGGGGG", 7],
#         [7, 3, "GGGHGGG", 2],
#         [7, 4, "HHGHGGG", 1],
#         [7, 4, "GHGHGGG", 2],
#         [4, 2, "GHGH", 2],
#         []
#         ]:
#     if run(n, k, cities)!= ans:
#         [print("---") for _ in range(3)]
#         print("Wrong")
#         val = run(n, k, cities)
#         print(f"Data: ", n, k, cities, ans, val)
#         break


