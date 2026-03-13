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

# begin x, y
bx, by = fx2, fy2
for i in range(fx1, fx2):
    for j in range(fy1, fy2):
        if arr[i][j] == True:  # 가장 작은 x, y 찾기
            if i < bx:
                bx = i
            if j < by:
                by = j
# print(bx, by)

# last x, y
lx, ly = bx, by
for i in range(fx1, fx2):
    for j in range(fy1, fy2):
        if arr[i][j] == True:  # 가장 큰 x, y 찾기
            if lx < i:
                lx = i
            if ly < j:
                ly = j

# 최소 직사각형의 넓이 구하기
cnt = 0
# print(bx, by, lx, ly)
if bx == lx and by != ly:  # 시작과 끝이 y만 다름
    for j in range(by, ly+1):
        cnt += 1
elif bx != lx and by == ly:  # 시작과 끝이 x만 다름
    for i in range(bx, lx+1):
        cnt += 1
elif bx != lx and by != ly:  # 시작과 끝이 x,y가 모두 다름
    for i in range(bx, lx+1):
        for j in range(by, ly+1):
            cnt += 1

print(cnt)