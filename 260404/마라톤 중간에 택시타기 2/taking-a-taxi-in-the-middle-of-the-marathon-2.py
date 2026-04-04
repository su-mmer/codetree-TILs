import sys

n = int(input())
checks = [list(map(int, input().split())) for _ in range(n)]

min_dis = sys.maxsize
for i in range(1, n-1):  # 건너뛸 부분 찾기
    dis = 0
    x1, y1 = checks[0][0], checks[0][1]  # 시작점

    for j in range(1, n): 
        if i == j:  # 건너뜀
            continue

        x2, y2 = checks[j][0], checks[j][1]  # 다음 도착지
        dis += abs(x1 - x2) + abs(y1 - y2)  # 택시거리 계산
        # print(x1, y1, x2, y2)
        x1, y1 = x2, y2

    min_dis = min(min_dis, dis)  # 최솟값 찾기
       
print(min_dis)