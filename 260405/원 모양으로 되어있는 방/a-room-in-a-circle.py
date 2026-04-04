import sys

n = int(input())
numbers = [int(input()) for _ in range(n)]

min_dis = sys.maxsize
for i in range(n):  #시작할 방
    dis = 0
    for j in range(n):  # 인원 계산
        d = j - i

        if d < 0:  # 방 번호가 한바퀴 돌아오면
            d = n - (-d)

        dis += numbers[j] * (d)  # 거리 계산
    
    min_dis = min(min_dis, dis)

print(min_dis)