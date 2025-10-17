pc, kc = input().split()
letters_coords = ["", "a", "b", "c", "d", "e", "f", "g", "h"]
starting_px = letters_coords.index(pc[0])
starting_py = int(pc[1])
starting_kx = letters_coords.index(kc[0])
starting_ky = int(kc[1])
def solve(starting_px, starting_py, starting_kx, starting_ky) -> float:
    # print(starting_px, [starting_py, starting_kx, starting_ky)
    ans = 1
    how_many_moves_to_queen_from_start = 8-starting_py
    pawn_positions = [y for y in range(starting_py, 9)]
    if starting_py +1 == starting_ky and (starting_px-1==starting_kx or starting_px+1==starting_kx):
        # print("eating on the first move")
        return 1
    if starting_py+1==starting_ky and starting_px==starting_kx:
        return 0.5

    dp = [set() for _ in range(how_many_moves_to_queen_from_start+1)]
    dp[0].add((starting_kx, starting_ky))

    for move_number in range(1, how_many_moves_to_queen_from_start+1):
        px = starting_px
        py = pawn_positions[move_number]
        for kx, ky in dp[move_number-1]:
            for dkx, dky in [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]:
                nkx = kx + dkx
                nky = ky + dky
                if nkx < 1 or nkx > 8 or nky < 1 or nky > 8:
                    continue
                if py+1 == nky and (px-1==nkx or px+1==nkx):
                    continue
                if move_number != how_many_moves_to_queen_from_start and nkx==px and nky==py+1:
                    ans = 0.5
                    continue
                if nkx==px and nky==py:
                    return -1
                dp[move_number].add((nkx, nky))
    # [print(*dp[i]) for i in range(how_many_moves_to_queen_from_start)]
    return ans
assert starting_py < 8
if starting_py != 2 or (starting_px==starting_kx and starting_ky==4):
    print(solve(starting_px, starting_py, starting_kx, starting_ky))
else:
    print(max(solve(starting_px, starting_py, starting_kx, starting_ky), solve(starting_px, starting_py+1, starting_kx, starting_ky)))




