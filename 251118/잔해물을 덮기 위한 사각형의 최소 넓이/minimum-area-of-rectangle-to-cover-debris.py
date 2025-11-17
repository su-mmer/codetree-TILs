OFFSET = 1000
arr = [ [ 0 for _ in range(OFFSET * 2 + 1) ] for _ in range(OFFSET * 2 + 1) ]

ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
ax1, ay1, ax2, ay2 = OFFSET+ax1, OFFSET+ay1, OFFSET+ax2, OFFSET+ay2
bx1, by1, bx2, by2 = OFFSET+bx1, OFFSET+by1, OFFSET+bx2, OFFSET+by2

# 채우기
for i in range(ay1, ay2):
    for j in range(ax1, ax2):
        arr[i][j] += 1

# 비우기
for i in range(by1, by2):
    for j in range(bx1, bx2):
        arr[i][j] -= 1

# 남은 잔해물을 덮기 위한 w, h
min_w, max_w = ax2, 0
for i in range(ay1, ay2):
    if 1 in arr[i] and arr[i].index(1) < min_w:
        min_w = arr[i].index(1)

    for j in range(ax1, ax2):
        if arr[i][j] == 1:
            max_w = j

w = 0
if max_w != 0:
    w = max_w - min_w + 1

min_h, max_h = ay2, 0
for j in range(ax1, ax2):
    for i in range(ay1, ay2):
        if arr[i][j] == 1:
            min_h = i
            break
    if min_h != ay2:
        break

for j in range(ax1, ax2):
    for i in range(ay1, ay2):
        if arr[i][j] == 1:
            max_h = i

h = 0
if max_h != 0:
    h = max_h - min_h + 1

# 넓이
print(w * h)