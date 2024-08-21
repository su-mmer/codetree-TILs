n, t = map(int, input().split())
r, c, d = input().split()
x, y = int(r), int(c)
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'U': 2,
    'D': 1,
    'R': 0,
    'L': 3
}

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


dir_num = mapper[d]  # 처음에 입력받은 방향
for i in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]  # 이동할 위치
    if not in_range(nx, ny):  # 해당 위치가 범위를 벗어났다면
        dir_num = 3 - dir_num  # 반대 방향으로 변경
    
    x, y = x + dxs[dir_num], y + dys[dir_num]

print(x+1, y+1)