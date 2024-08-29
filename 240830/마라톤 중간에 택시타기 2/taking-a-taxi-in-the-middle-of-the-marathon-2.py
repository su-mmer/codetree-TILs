import sys

MAX_INT = sys.maxsize  # 최대 크기

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_num = MAX_INT  # 최대 크기를 미리 넣어서 비교하게 함
d = 0  # distance
for i in range(1, n - 1):
    temp = arr[:i] + arr[i+1:n]  # 1번, N번 체크포인트 제외한 배열
    for j in range(n - 2):  # 거리 계산
        d += abs(temp[j][0] - temp[j+1][0]) + abs(temp[j][1] - temp[j+1][1])
    min_num = min(min_num, d)  # 최소값 비교

print(min_num)