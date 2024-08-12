OFFSET = 100
n = int(input())
arr = [[0 for _ in range(201)] for _ in range(201)]

for _ in range(n):
    x, y = map(int, input().split())
    x += OFFSET
    y += OFFSET
    
    for i in range(x, x+8):
        for j in range(y, y+8):
            arr[i][j] = 1

count = 0
for elem in arr:
    for c in elem:
        if c == 1:
            count += 1

print(count)