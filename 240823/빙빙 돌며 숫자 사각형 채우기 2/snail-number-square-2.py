# 갈 방향에 대해 범위 내인지 확인
# 범위를 벗어났거나 이미 갔던 곳이면 오른쪽으로 돌기 (dir_num+3)%4
# n*m번

n, m = map(int, input().split())
arr = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 격자
x, y = 0, 0  # 시작 위치
dir_num = 1  # 시작 방향 (아래)
arr[x][y] = 1  # 초기값 1
for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 3) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()