import sys
arr = list(map(int, input().split()))
team_a, team_b = 0, 0

def calculate(x, y, z):
    team_a = arr[x] + arr[y] + arr[z]
    team_b = sum(arr) - team_a
    return abs(team_a - team_b)

min_cost = sys.maxsize
for x in range(6):
    for y in range(x + 1, 6):
        for z in range(y + 1, 6):
            min_cost = min(min_cost, calculate(x, y, z))

print(min_cost)