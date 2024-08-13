n = int(input())
arr = [[0 for _ in range(201)] for _ in range(201)]
flag = True

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    color = 'r' if flag else 'b'
    
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = color

    flag = False if flag else True

answer = 0
for elem in arr:
    for c in elem:
        if c == 'b': answer += 1

print(answer)