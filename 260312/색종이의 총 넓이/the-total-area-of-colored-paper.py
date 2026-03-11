n = int(input())
OFFSET = 100
blocks = [[False for _ in range(OFFSET * 2 + 1)] for _ in range(OFFSET * 2 + 1)]

for _ in range(n):
    x1, y1 = map(int, input().split())
    x1, y1 = OFFSET+x1, OFFSET+y1

    for i in range(x1, x1+8):
        for j in range(y1, y1+8):
            blocks[i][j] = True


cnt = 0
for elem in blocks:
    for e in elem:
        if e == True:
            cnt += 1
    
print(cnt)