n = int(input())
OFFSET = 100
arr = [ [ 0 for _ in range(OFFSET * 2 + 1)] for _ in range(OFFSET * 2 + 1)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + OFFSET, y1 + OFFSET, x2 + OFFSET, y2 + OFFSET
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] += 1
    
cnt = 0
for row in arr:
    for elem in row:
        if elem >= 1:
            cnt += 1

print(cnt)