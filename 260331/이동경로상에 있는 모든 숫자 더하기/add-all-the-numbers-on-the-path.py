n, t = map(int, input().split())
orders = list(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


x, y = n // 2, n // 2  # 초기 위치
move_dir = 3  # 초기 방향
answer = arr[x][y]  # 정답 

for o in orders:
    if o == 'L':
        move_dir = (move_dir + 3) % 4
    elif o == 'R':
        move_dir = (move_dir + 1) % 4
    elif o == 'F':
        nx, ny = x + dxs[move_dir], y + dys[move_dir]

        if not in_range(nx, ny):
            continue  # 범위 초과시 무시

        x, y = nx, ny
        # print(arr[x][y], answer)
        answer += arr[x][y]

print(answer)