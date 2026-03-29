n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

x, y = n-1, n-1  # 큰 값부터 입력
move_dir = 2
arr[x][y] = n * n
for i in range(1, n * n):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        move_dir = (move_dir + 1) % 4
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

    x, y = nx, ny
    arr[x][y] = n * n -i

for elem in arr:
    for e in elem:
        print(e, end=' ')
    print()