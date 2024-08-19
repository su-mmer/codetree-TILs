n = int(input())
arr = [[] for _ in range(n)]
dxs, dys = [0, 1 ,0, -1], [1, 0, -1, 0]
# x, y = 0, 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 격자 입력
for i in range(n):
    arr[i] = list(map(int, input().split()))

cnt = 0
for x in range(n):
    for y in range(n):
        one = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                one += 1
            if one == 3:
                cnt += 1
                break

print(cnt)