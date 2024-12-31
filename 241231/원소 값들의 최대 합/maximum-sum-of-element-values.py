# 1~n 수열
# 움직임: 시작위치를 정하고 index에 위치한 원소를 index로 하여 이동
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_mv = 0  # 움직임 원소값 합의 최대
for i in range(1, n):  # 배열 전체 탐색 (시작 위치)
    cp = arr[:]  # array init
    sum_mv = 0  # 원소값 합 init
    for j in range(m):  # m번 움직임
        mv = cp[i]
        cp[i], cp[mv] = cp[mv], mv  # swap
        sum_mv += mv  # 움직임 원소값 합
    max_mv = max(max_mv, sum_mv)  # 최대 비교

print(max_mv)