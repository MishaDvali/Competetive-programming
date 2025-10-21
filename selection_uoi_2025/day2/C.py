n, m = list(map(int, input().split()))
calendar = [input() for _ in range(n)]
# n = 4
# m = 3
# calendar = [
#         "#.#",
#         "###",
#         "#.#",
#         "#..",
#         ]

opened = "."
closed = "#"
all_zeroes="0"*m


# 0: - 
# 1: |

def calc_sticks(b_this, b_last, row, n_this, n_last)-> int:
    # print(f"clac_sticks {b_this, b_last, calendar, curr_row_index}", end=" ")
    sticks_used = 0
    horizontal = False
    for i in range(m):
        if row[i]==opened:
            horizontal=False 
            continue
        if horizontal:
            if b_this[i] == "0": 
                continue
        elif b_this[i] == "0":
            horizontal=True
            sticks_used+=1 
            continue

        horizontal=False
        if b_this[i]== "1":
            if b_last[i]=="0": 
                sticks_used+=1
    # print(sticks_used)
    cache[n_this][n_last]=sticks_used
    return sticks_used

def calc_dp_for_var(n_var_repr, b_var_repr, dp, bin_layer, dp_last_layer, b_last_layer, calendar, current_row_index):
    # [print("---"*3) for i in range(2)]
    # print(f"calc_dp_for_var({n_var_repr}, {b_var_repr}, {dp}, {bin_layer}, {dp_last_layer, b_last_layer, calendar, current_row_index})")
    # print("---"*3)
    minimum = 100000
    for n_repr_last_layer in range(2**m):
        new_dp_val = (dp_last_layer[n_repr_last_layer] +
                      calc_sticks(b_var_repr, b_last_layer[n_repr_last_layer], calendar[current_row_index], n_var_repr, n_repr_last_layer))
        minimum = min(minimum, new_dp_val)

    return minimum

def calc_dp(dp, b_layer_repr, dp_last_layer, b_last_layer, calendar, current_row_index):
    # print(f"Generating new dp layer {dp, b_layer_repr, dp_last_layer, b_last_layer, calendar, current_row_index}")
    for n_var_repr in range(2**m): 
        b_unformatted = bin(n_var_repr)[2:]
        b_var_repr = "0"*(m-len(b_unformatted))+b_unformatted
        has_ones_where_should_be_zeroes = False
        for i in range(m):
            if b_var_repr[i]=="1" and calendar[current_row_index][i] == ".":
                has_ones_where_should_be_zeroes=True
                break
        if has_ones_where_should_be_zeroes: 
            dp[n_var_repr] = 10000
            b_layer_repr[n_var_repr]=all_zeroes
            continue
        b_layer_repr[n_var_repr]=b_var_repr
        dp[n_var_repr]=calc_dp_for_var(n_var_repr, b_var_repr, dp, b_layer_repr, dp_last_layer, b_last_layer, calendar, current_row_index)

            

def solve():
    current_row_index = 0
    dp_last_layer = [0 for _ in range(2**m)]
    dp_new_layer = [0 for _ in range(2**m)]
    b_last_layer = ["0"*m for _ in range(2**m)]
    b_new_layer = ["" for _ in range(2**m)]
    for i in range(n):
        # [print("---"*3) for _ in range(3)]
        calc_dp(dp_new_layer, b_new_layer, dp_last_layer, b_last_layer, calendar, current_row_index)
        # print("NEW DP LAYER GENERATED")
        # print(dp_new_layer)
        temp = dp_last_layer
        dp_last_layer = dp_new_layer
        dp_new_layer = temp

        temp = b_last_layer
        b_last_layer = b_new_layer
        b_new_layer = temp
        current_row_index+=1

    print(min(dp_last_layer))

# def test(func, expected, args):
#     val = func(*args)
#     if val!=expected:
#         print("-"*10)
#         print("Failed:", func)
#         print("Expected:", expected, "Got: ", val)
#         print("Args:", args)


#calc sticks tests
# test(calc_sticks, 1, ['100', '000', ['.##', '##.'], 0])

# cs_cal1 = [
#         "#.#",
#         "###",
#         "..."
#         ]
# test(calc_sticks, 2, ["101", "000", cs_cal1, 0])
# test(calc_sticks, 2, ["100", "000", cs_cal1, 0])
# test(calc_sticks, 2, ["110", "000", cs_cal1, 0])
# test(calc_sticks, 2, ["001", "000", cs_cal1, 0])
#
# test(calc_sticks, 1, ["101", "101", cs_cal1, 1])
# test(calc_sticks, 1, ["000", "101", cs_cal1, 1])
# test(calc_sticks, 1, ["100", "101", cs_cal1, 1])
# test(calc_sticks, 1, ["001", "101", cs_cal1, 1])
#
# test(calc_sticks, 2, ["101", "001", cs_cal1, 1])
# test(calc_sticks, 1, ["000", "001", cs_cal1, 1])
# test(calc_sticks, 2, ["100", "001", cs_cal1, 1])
# test(calc_sticks, 1, ["000", "101", cs_cal1, 1])
#
# test(calc_sticks, 0, ["101", "101", cs_cal1, 2])
# test(calc_sticks, 0, ["101", "101", cs_cal1, 2])
# test(calc_sticks, 0, ["101", "101", cs_cal1, 2])
# test(calc_sticks, 0, ["101", "101", cs_cal1, 2])
# test(calc_sticks, 0, ["101", "101", cs_cal1, 2])
#
# test(calc_sticks, 1, ["000", "001", cs_2, 0])
# test(calc_sticks, 1, ["001", "001", cs_2, 0])
# test(calc_sticks, 1, ["010", "001", cs_2, 0])
# test(calc_sticks, 1, ["011", "001", cs_2, 0])
# test(calc_sticks, 1, ["100", "001", cs_2, 0])
# test(calc_sticks, 1, ["101", "001", cs_2, 0])
# test(calc_sticks, 1, ["110", "001", cs_2, 0])
# test(calc_sticks, 1, ["111", "001", cs_2, 0])
#
# test(calc_sticks, 1, ["000", "011", cs_2, 0])
# test(calc_sticks, 1, ["001", "011", cs_2, 0])
# test(calc_sticks, 1, ["010", "011", cs_2, 0])
# test(calc_sticks, 1, ["011", "011", cs_2, 0])
# test(calc_sticks, 1, ["100", "011", cs_2, 0])
# test(calc_sticks, 1, ["101", "011", cs_2, 0])
# test(calc_sticks, 1, ["110", "011", cs_2, 0])
# test(calc_sticks, 1, ["111", "011", cs_2, 0])
# test(calc_sticks, 1, ["101", "000", cs_cal1, 0])
solve()
