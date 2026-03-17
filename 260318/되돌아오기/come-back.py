x, y = 0, 0
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

n = int(input())

time, clear = 0, False
for _ in range(n):
    w, d = input().split()
    d = int(d)

    if w == 'E':
        move_dir = 0
    elif w == 'S':
        move_dir = 1
    elif w == 'W':
        move_dir = 2
    elif w == 'N':
        move_dir = 3

    for i in range(d):
        x = x + dxs[move_dir]
        y = y + dys[move_dir]
        time += 1

        if x == 0 and y == 0:
            clear = True

    if clear: break

print(time) if clear else print(-1)