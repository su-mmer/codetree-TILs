n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


move_dir = 0
x, y = 0, 0
arr[0][0] = 'A'
for i in range(n * m - 1):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    if not in_range(nx, ny) or arr[nx][ny] != 0:  # 범위 벗어나거나 이미 입력된 칸을 만나면
        move_dir = (move_dir + 1) % 4  # 방향 변경
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

    arr[nx][ny] = chr(ord(arr[x][y]) + 1)  # 알파벳 + 1

    if arr[x][y] == 'Z':
        arr[nx][ny] = 'A'

    x, y = nx, ny


for elem in arr:
    for e in elem:
        print(e, end=' ')
    print()