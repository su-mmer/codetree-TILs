ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())
arr = [[0 for _ in range(2001)] for _ in range(2001)]

for i in range(ax1, ax2):
    for j in range(ay1, ay2):
        arr[i][j] = 1

for i in range(bx1, bx2):
    for j in range(by1, by2):
        arr[i][j] = 1

for i in range(mx1, mx2):
    for j in range(my1, my2):
        arr[i][j] = 0

count = 0
for i in range(2001):
    for j in range(2001):
        if arr[i][j] == 1:
            count += 1

print(count)