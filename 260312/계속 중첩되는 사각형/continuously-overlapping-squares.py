OFFSET = 100
blocks = [[False for _ in range(OFFSET * 2 + 1)] for _ in range(OFFSET * 2 + 1)]

n = int(input())

red = True  # 컬러 구분
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if red:
                blocks[i][j] = False
            else:
                blocks[i][j] = True
    red = False if red else True  # red 값 True <-> False 교체

# 넓이 계산   
cnt = 0
for elem in blocks:
    for e in elem:
        if e == True:
            cnt += 1

print(cnt)