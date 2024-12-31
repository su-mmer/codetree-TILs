n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_mv = 0  # 움직임 원소값 합의 최대
for i in range(1, n + 1):  # 배열 전체 탐색 (시작 위치)
    mv = arr[i]  # 처음 원소 init
    sum_mv = 0  # 원소값 합 init
    for _ in range(m):  # m번 움직임
        sum_mv += mv  # 움직임 원소값 합
        mv = arr[mv]
    max_mv = max(max_mv, sum_mv)  # 최대 비교

print(max_mv)