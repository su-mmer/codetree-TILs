import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = sys.maxsize
for i in range(n):  # i가 최대일 때
    cost = 0
    for j in range(n):
        if arr[i] < arr[j]:  # 내가 정한 최대값보다 클 경우 최대값 크기로 맞춰줌
            cost += arr[j] - arr[i]
        elif arr[i] - arr[j] > k:  # 최대값과 해당 값의 차가 k 보다 큼, 무조건 arr[i]가 더 큼
            cost += arr[i] - arr[j] - k
    min_cost = min(min_cost, cost)

print(min_cost)