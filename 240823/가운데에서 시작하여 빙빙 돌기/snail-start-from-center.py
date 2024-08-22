n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 격자
x, y = n-1, n-1  # 시작 위치
dir_num = 2  # 시작 방향 (오른쪽)
arr[x][y] = n * n  # 시작 위치의 값

for i in range(n * n - 1, 0, -1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()