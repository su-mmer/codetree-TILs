n = int(input())
arr = [0 for _ in range(1001)]  # 전체 구간
point = 0  # 현재 위치

for _ in range(n):
    a, b = input().split()
    a = int(a)
    # 왼쪽 이동
    if b == "L":
        # 현재 위치 - a ~ 현재 위치까지 +1
        for i in range(point - a, point):
            arr[i] += 1
        # 현재 위치 이동
        point -= a
    # 오른쪽 이동
    elif b == "R":
        for i in range(point, point + a):
            arr[i] += 1
        point += a

value = 0  # 출력할 정답
# 2번 이상 지나갔으면 +1
for i in range(len(arr)):
    if arr[i] >= 2:
        value += 1

print(value)