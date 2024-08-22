n, m = map(int, input().split())
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]  # 칠해지지 않은 0, 칠해지면 1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]  # 격자

# 범위 내에 있는지 판별
def in_range(x, y):
    return 0 < x and x < n + 1 and 0 < y and y < n + 1


# 편안한 상태인지 판별
def is_calm(x, y):

    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = r + dx, c + dy
        # 4면이 범위 내에 있으며 cnt가 3일 경우
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1

    return True if cnt == 3 else False


for i in range(m):
    r, c = map(int, input().split())  # 색칠할 위치
    arr[r][c] = 1  # 칸 색칠

    print(int(is_calm(r, c)))