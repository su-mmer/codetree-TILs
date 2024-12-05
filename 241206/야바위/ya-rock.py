n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_cost = 0
for p in range(1, 4):
    yabawee = [0, 0, 0, 0]  # 종이컵
    yabawee[p] = 1  # 조약돌의 위치
    cost = 0  # 점수
    for i in range(n):  # N번 돌면서 게임 시작
        a, b, c = arr[i][0], arr[i][1], arr[i][2]
        yabawee[a], yabawee[b] = yabawee[b], yabawee[a]  # 야바위
        if yabawee[c] == 1:  # 조약돌 있으면 점수
            cost += 1
    max_cost = max(max_cost, cost)

print(max_cost)