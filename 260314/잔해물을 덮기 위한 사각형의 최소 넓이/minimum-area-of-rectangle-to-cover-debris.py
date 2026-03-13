OFFSET = 1000  # 양수 변환 기준 수
arr = [[False for _ in range(OFFSET * 2 + 1)] for _ in range(OFFSET * 2 + 1)]

# 입력
fx1, fy1, fx2, fy2 = map(int, input().split())
sx1, sy1, sx2, sy2 = map(int, input().split())
fx1, fy1, fx2, fy2 = fx1+OFFSET, fy1+OFFSET, fx2+OFFSET, fy2+OFFSET
sx1, sy1, sx2, sy2 = sx1+OFFSET, sy1+OFFSET, sx2+OFFSET, sy2+OFFSET

# 첫 번째 직사각형
for i in range(fx1, fx2):
    for j in range(fy1, fy2):
        arr[i][j] = True

# 두 번째 직사각형
for i in range(sx1, sx2):
    for j in range(sy1, sy2):
        arr[i][j] = False

# begin, last x, y
bx, by, lx, ly = fx2, fy2, fx1, fy1
hasTrue = False  # 덮어야 하는 사각형 확인
for i in range(fx1, fx2):
    for j in range(fy1, fy2):
        if arr[i][j] == True:  # 가장 작은, 가장 큰 xy 찾기
            hasTrue = True
            bx = min(i, bx)
            by = min(j, by)
            lx = max(i, lx)
            ly = max(j, ly)
# print(bx, by, lx, ly)

# 최소 직사각형의 넓이 구하기
cnt = 0
if hasTrue:  # 덮어야 하는 사각형이 있으면
    cnt = (lx - bx + 1) * (ly - by + 1)

print(cnt)