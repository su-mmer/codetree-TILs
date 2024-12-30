# 3개의 종이컵
# swap(a종이컵, b종이컵) n회
# c번 종이컵을 열어 조약돌이 있으면 점수 획득
n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]

max_scr = 0  # 가장 높은 점수
for i in range(1, 4):  # 1, 2, 3 중 어느 위치
    score = 0  # 야바위 점수 init
    place = [0, 0, 0, 0]  # 종이컵 init
    place[i] = 1  # 조약돌 배치
    for elem in arr:
        a, b, c = elem[0], elem[1], elem[2]
        place[a], place[b] = place[b], place[a]  # swap
        if place[c]:
            score += 1  # 조약돌 있으면 점수 get
    max_scr = max(max_scr, score)

print(max_scr)