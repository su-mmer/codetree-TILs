n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


move_dir = 1
arr[0][0] = 1
x, y = 0, 0
for i in range(2, n * m + 1):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]

    if not in_range(nx, ny) or arr[nx][ny] != 0:  # 범위 벗어나거나 이미 채워진 칸을 만나면
        move_dir = (move_dir + 3) % 4  # 이동
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
    arr[nx][ny] = i
    x, y = nx, ny
        

for elem in arr:
    for e in elem:
        print(e, end=' ')
    print()