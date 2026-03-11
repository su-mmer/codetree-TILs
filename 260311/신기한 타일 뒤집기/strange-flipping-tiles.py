n = int(input())
OFFSET = 1000*100
blocks = [0 for _ in range(OFFSET * 2 + 2)]

p = OFFSET
for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == 'R':
        for i in range(p, p+x):
            blocks[i] = 'b'
        p += x-1
    if d == 'L':
        for i in range(p, p-x, -1):
            blocks[i] = 'w'
        p -= x-1

# 값 출력
black, white = 0, 0
for i in blocks:
    if i == 'b':
        black += 1
    elif i == 'w':
        white += 1

print(white, black)