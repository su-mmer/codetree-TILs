ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
cx1, cy1, cx2, cy2 = map(int, input().split())
arr = [ [0 for _ in range(2001)] for _ in range(2001) ]

for i in range(2001):
    for j in range(2001):
        if ax1 <= i and i < ax2 and ay1 <= j and j < ay2:
            arr[i][j] += 1
        if bx1 <= i and i < bx2 and by1 <= j and j < by2:
            arr[i][j] += 1
        if cx1 <= i and i < cx2 and cy1 <= j and j < cy2:
            arr[i][j] -= 1

cnt = 0
for row in arr:
    for elem in row:
        if elem == 1:
            cnt += 1

print(cnt)