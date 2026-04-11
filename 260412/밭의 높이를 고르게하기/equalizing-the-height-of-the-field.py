import sys

n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = sys.maxsize  # 최소 비용
for i in range(n - t + 1):
    cost = 0
    for j in range(i, i + t):  # 일정 구간
        cost += abs(arr[j] - h)  # h 높이로 맞추기 위한 비용 계산

    min_cost = min(min_cost, cost)

print(min_cost)