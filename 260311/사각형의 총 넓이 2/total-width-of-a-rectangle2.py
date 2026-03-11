n = int(input())
OFFSET = 100
blocks = [[0 for _ in range(OFFSET * 2 + 1)] for _ in range(OFFSET * 2 + 1)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = OFFSET+x1, OFFSET+y1, OFFSET+x2, OFFSET+y2  # 양수 변환

    for i in range(x1, x2):
        for j in range(y1, y2):
            blocks[i][j] += 1

# 모든 넓이 계산
cnt = 0
for elem in blocks:
    for e in elem:
        if e > 0:
            cnt += 1

print(cnt)