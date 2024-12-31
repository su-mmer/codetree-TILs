n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_mv = 0  # 움직임 원소값 합의 최대
for i in range(1, n):  # 배열 전체 탐색 (시작 위치)
    cp = arr[:]  # array init
    mv = cp[i]
    sum_mv = 0  # 원소값 합 init
    for j in range(m):  # m번 움직임
        # print(mv)
        # mv = cp[i]
        # print(cp[i], cp[mv], cp[mv], mv)
        cp[i], cp[mv] = cp[mv], mv  # swap
        print(cp[i], cp[mv], cp)
        sum_mv += mv  # 움직임 원소값 합
        mv = cp[i]
        # print(cp)
    print(sum_mv)
    max_mv = max(max_mv, sum_mv)  # 최대 비교

print(max_mv)