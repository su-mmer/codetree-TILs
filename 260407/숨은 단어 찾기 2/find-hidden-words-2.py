n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
nxs, nys = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]  # 8 방향 확인

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m


cnt = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':  # L 찾으면
            for x, y in zip(nxs, nys):  # 8방향 비교
                # E E 찾기
                if in_range(i+x, j+y) and in_range(i+2*x, j+2*y) and arr[i+x][j+y] == 'E' and arr[i+2*x][j+2*y] == 'E':
                    cnt += 1

print(cnt)