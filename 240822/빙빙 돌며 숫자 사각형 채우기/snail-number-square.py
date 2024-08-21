n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 격자

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


dir_num = 0  # 방향
x, y = 0, 0  # 시작 위치
arr[x][y] = 1  # 초기값
for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

# 출력
for i in range(n):
    for j in range(m):
        print(arr[i][j], end=' ')
    print()