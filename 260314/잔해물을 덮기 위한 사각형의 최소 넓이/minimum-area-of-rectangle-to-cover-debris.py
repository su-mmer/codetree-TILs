OFFSET = 1000
arr = [[False for _ in range(OFFSET * 2 + 1)] for _ in range(OFFSET * 2 + 1)]

fx1, fy1, fx2, fy2 = map(int, input().split())
sx1, sy1, sx2, sy2 = map(int, input().split())
fx1, fy1, fx2, fy2 = fx1+OFFSET, fy1+OFFSET, fx2+OFFSET, fy2+OFFSET
sx1, sy1, sx2, sy2 = sx1+OFFSET, sy1+OFFSET, sx2+OFFSET, sy2+OFFSET

for i in range(fx1, fx2):
    for j in range(fy1, fy2):
        arr[i][j] = True

for i in range(sx1, sx2):
    for j in range(sy1, sy2):
        arr[i][j] = False

bx, by = fx2, fy2
for i in range(fx1, fx2):
    for j in range(fy1, fy2):
        if arr[i][j] == True:
            if i < bx:
                bx = i
            if j < by:
                by = j
# print(bx, by)

lx, ly = bx, by
# print(bx, by, lx, ly)
for i in range(fx1, fx2):
    for j in range(fy1, fy2):
        if arr[i][j] == True:
            if lx < i:
                lx = i
            if ly < j:
                ly = j

cnt = 0
# print(bx, by, lx, ly)
if bx == lx and by != ly:
    # for i in range(bx, lx+1):
    for j in range(by, ly+1):
        cnt += 1
elif bx != lx and by == ly:
    for i in range(bx, lx+1):
        # for j in range(by, ly+1):
        cnt += 1
elif bx != lx and by != ly:
    for i in range(bx, lx+1):
        for j in range(by, ly+1):
            cnt += 1

print(cnt)