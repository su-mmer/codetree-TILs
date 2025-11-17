OFFSET = 1000
arr = [ [ 0 for _ in range(OFFSET * 2 + 1) ] for _ in range(OFFSET * 2 + 1) ]

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
ax1, ay1, ax2, ay2 = OFFSET+ax1, OFFSET+ay1, OFFSET+ax2, OFFSET+ay2
bx1, by1, bx2, by2 = OFFSET+bx1, OFFSET+by1, OFFSET+bx2, OFFSET+by2

for i in range(ay1, ay2):
    for j in range(ax1, ax2):
        arr[i][j] += 1

for i in range(by1, by2):
    for j in range(bx1, bx2):
        arr[i][j] -= 1

# 가로
max_w = 0
for i in range(ay1, ay2):
    cnt = 0
    for j in range(ax1, ax2):
        if arr[i][j] == 1:
            cnt += 1
    if max_w < cnt:
        max_w = cnt 

# 세로
max_h = 0
for j in range(ax1, ax2):
    cnt = 0
    for i in range(ay1, ay2):
        if arr[i][j] == 1:
            cnt += 1
    if max_h < cnt:
        max_h = cnt

print(max_w * max_h)