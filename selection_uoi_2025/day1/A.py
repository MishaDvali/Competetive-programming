cow, m = tuple(map(int, input().split()))
segments = sorted([sorted(list(map(int, input().split()))) for _ in range(m)])
# print("--")
# print(f"cows: {cow}, m: {m}")
# print(segments)
# print("--")

best_d=None
# print(segments[-1][-1], segments[0][0])

def check_d(cow, segments, d):
    print(f"d:{d}")
    pos = segments[0][0] - d
    segment_index = 0

    for cows_left in range(cow, 0, -1):
        print(f"cows_left: {cows_left}, pos: {pos}, segment_index:{segment_index}")
        have_found_segment = False
        for new_segment_index in range(segment_index, len(segments)):
            if pos+d <= segments[new_segment_index][0]:
                segment_index = new_segment_index
                pos = segments[new_segment_index][0]
                print(f"On a segment {segments[segment_index]}, pos: {pos}")
                segment_index =new_segment_index
                have_found_segment = True
                break
            if pos+d <= segments[new_segment_index][1]:
                print(f"On a segment {segments[segment_index]}, pos: {pos}")
                segment_index =new_segment_index
                pos = pos+d
                have_found_segment = True
                break
        if not have_found_segment:
            return
    return True

low = 1
high = (segments[-1][1] - segments[0][0] + 1) // cow + 1

mid=None
best_d = None
while low < high:
    print(low, high)
    mid = (low+high)//2
    if not check_d(cow, segments, mid):
        high = mid
    else:
        best_d = mid
        low=mid +1
mid = (low+high)//2
if not check_d(cow, segments, mid):
    high = mid
else:
    best_d = mid
    low=mid
if check_d(cow, segments, best_d+1):
    best_d=best_d+1

print(best_d)





