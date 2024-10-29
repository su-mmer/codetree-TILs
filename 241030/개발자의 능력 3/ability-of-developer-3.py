import sys
arr = list(map(int, input().split()))
team_a, team_b = 0, 0

ability = 0
min_cost = sys.maxsize
for x in range(6):
    for y in range(x + 1, 6):
        for z in range(y + 1, 6):
            team_a = x + y + z
            team_b = sum(arr) - team_a
            ability = abs(team_a - team_b)
        min_cost = min(min_cost, ability)

print(min_cost)