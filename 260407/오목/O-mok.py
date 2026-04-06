n, m = 19, 19
arr = [list(map(int, input().split())) for _ in range(n)]
nxs, nys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]  # 8 방향 확인

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

win = 0
flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and not flag:
            c = arr[i][j]  # color
            
            for x, y in zip(nxs, nys):
                nx, ny = i + x, j + y
                flag = True

                for t in range(4):
                    if in_range(nx, ny) and arr[nx][ny] == c:
                        # print(c, i, j, nx, ny, arr[nx][ny], win, flag)
                        nx, ny = nx + x, ny + y
                    else:
                        flag = False
                        break
                if flag:
                    win = c
                    # print(i, j, nx, ny)
                    a, b = nx - (3 * x) + 1, ny - (3 * y) + 1
                    break

if win != 0:
    print(win)
    print(a, b)
else:
    print(win)