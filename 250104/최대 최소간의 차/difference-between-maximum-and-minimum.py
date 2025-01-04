import sys

n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_cost = sys.maxsize
for i in range(n):  # arr[i]에 대한 계산
    # arr[i]를 최대값으로 가정
    cost = 0
    for j in range(n):
        if arr[i] < arr[j]:  # 내가 정한 최대값보다 클 경우 최대값 크기로 맞춰줌
            cost += arr[j] - arr[i]
        elif arr[i] - arr[j] > k:  # 최대값과 해당 값의 차가 k 보다 큼, 무조건 arr[i]가 더 큼
            cost += arr[i] - arr[j] - k

    min_cost = min(min_cost, cost)

    # arr[i]를 최소값으로 가정
    cost = 0
    for j in range(n):
        if arr[i] > arr[j]:  # arr[j]가 더 작을 경우 내가 정한 최소값으로 맞춰줌
            cost += arr[i] - arr[j]
        elif arr[j] - arr[i] > k:  # arr[j]와의 차가 k보다 클 경우
            cost += arr[j] - arr[i] - k

    min_cost = min(min_cost, cost)

print(min_cost)