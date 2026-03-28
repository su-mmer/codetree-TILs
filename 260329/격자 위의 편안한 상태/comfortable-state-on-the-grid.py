n, m = map(int, input().split())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
arr = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

def in_range(x, y):  # 범위 확인
    return 0 < x and x <= n and 0 < y and y <= n


for _ in range(m):
    r, c = map(int, input().split())
    arr[r][c] = 1  # 칸 색칠

    cnt = 0
    for i in range(4):  # 인접한 칸 확인
        rn, cn = r + dxs[i], c + dys[i]
        if in_range(rn, cn) and arr[rn][cn]==1:
            cnt += 1

    print(1) if cnt == 3 else print(0)
