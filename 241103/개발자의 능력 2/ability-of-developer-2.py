import sys
arr = list(map(int, input().split()))
n = 6

# 가장 높은 팀 - 가장 낮은 팀
def calc_diff(one, two, three):
    max_val = -sys.maxsize
    min_val = sys.maxsize
    max_val = max(one, two)
    max_val = max(max_val, three)
    min_val = min(one, two)
    min_val = min(min_val, three)

    return max_val - min_val

# 2명씩 2팀을 고르면 나머지는 합에서 뺀 값
# diff_val = 0
min_diff = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        team_one = arr[i] + arr[j]
        for k in range(n):
            for l in range(k+1, n):
                if k == i or k == j or l == i or l == j:
                    continue
                team_two = arr[k] + arr[l]
                team_three = sum(arr) - team_one - team_two
                # print(arr[i], arr[j], arr[k], arr[l])
                # print(arr[k], arr[l])
                # diff_val = calc_diff(team_one, team_two, team_three)
                # print(team_one, team_two, team_three, diff_val)
                min_diff = min(calc_diff(team_one, team_two, team_three), min_diff)

print(min_diff)