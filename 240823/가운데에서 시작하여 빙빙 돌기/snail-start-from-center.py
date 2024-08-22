n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

# 격자를 벗어나는지 판단
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 격자
x, y = n-1, n-1  # 시작 위치
dir_num = 2  # 시작 방향 (왼쪽)
arr[x][y] = n * n  # 시작 위치의 값

# 마지막 칸부터 안쪽으로 돌면서 채우기
for i in range(n * n - 1, 0, -1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]  # 이동할 자리
    # 이동할 자리가 범위를 벗어났거나 값이 있으면 방향 전환
    if not in_range(nx, ny) or arr[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    arr[x][y] = i

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()