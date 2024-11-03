import sys
n = 5
arr = list(map(int, input().split()))

def calc_diff(one, two, three):
    # same score => continue
    if team_1 == team_2 or team_2 == team_3 or team_3 == team_1:
        return -1
    # not same score => calculate difference
    max_val = max(one, two)
    max_val = max(max_val, three)
    min_val = min(one, two)
    min_val = min(min_val, three)

    return max_val - min_val

min_val = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        team_1 = arr[i] + arr[j]
        for k in range(n):
            if k == i or k == j:
                continue
            team_3 = arr[k]
            team_2 = sum(arr) - team_1 - team_3
            # same score => continue
            # if team_1 == team_2 or team_2 == team_3 or team_3 == team_1:
                # continue
            # not same score => calculate difference
            min_val = min(calc_diff(team_1, team_2, team_3), min_val)

print(min_val)