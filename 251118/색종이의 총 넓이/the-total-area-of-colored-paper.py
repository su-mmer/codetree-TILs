n = int(input())
OFFSET = 100
arr = [ [ 0 for _ in range(OFFSET * 2 + 1) ] for _ in range(OFFSET * 2 + 1) ]

for _ in range(n):
    x, y = map(int, input().split())
    x, y = OFFSET + x, OFFSET + y

    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j] += 1


cnt = 0
for row in arr:
    for elem in row:
        if elem > 0:
            cnt += 1

print(cnt)