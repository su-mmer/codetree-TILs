n = int(input())
arr = [list(input()) for _ in range(n)]
k = int(input())  # 레이저를 쏘는 위치

# 레이저 위치 (x,y) 찾기
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


kxs, kys = [0, 1, 0, -1], [1, 0, -1, 0]
kx, ky = 0, 0
move_dir = 0  # 레이저 돌리기
init_dir = 0  # 처음 시작하는 모서리 위치
for _ in range(1, k):
    nkx, nky = kx + kxs[move_dir], ky + kys[move_dir]

    if not in_range(nkx, nky):
        move_dir = (move_dir + 1) % 4
        nkx, nky = kx, ky
        init_dir += 1
    
    kx, ky = nkx, nky  # 시작하는 위치


# print(kx, ky, init_dir)

# 시작하는 move_dir을 찾기 위해 모서리와 / \ 확인
if init_dir == 0 and arr[kx][ky] == '/':
    move_dir = 0
elif init_dir == 0 and arr[kx][ky] == '\\':
    move_dir = 2
elif init_dir == 1 and arr[kx][ky] == '/':
    move_dir = 3
elif init_dir == 1 and arr[kx][ky] == '\\':
    move_dir = 3
elif init_dir == 2 and arr[kx][ky] == '/':
    move_dir = 1
elif init_dir == 2 and arr[kx][ky] == '\\':
    move_dir = 0
elif init_dir == 3 and arr[kx][ky] == '/':
    move_dir = 2
elif init_dir == 3 and arr[kx][ky] == '\\':
    move_dir = 1

# print(init_dir, move_dir)

# left_x, left_y = [1, -1, 0, 0], [0, 0, 1, -1]  # /인 경우 회전 방향
# right_x, right_y = [-1, 0, 1, 0], [0, 1, 0, -1]  # \인 경우 회전 방향
cnt = 0

# while in_range(kx, ky):
#     if arr[kx][ky] == '/':  # left
#         move_dir = (3 - move_dir) % 4
#         kx, ky = kx + left_x[move_dir], ky + left_y[move_dir]
        
#     elif arr[kx][ky] == '\\':  # right
#         move_dir = (3 - move_dir) % 4
#         kx, ky = kx + right_x[move_dir], ky + right_y[move_dir]

#     cnt += 1

left_x, left_y = [0, -1, 0, 1], [-1, 0, 1, 0]  # /인 경우 회전 방향
right_x, right_y = [-1, 0, 1, 0], [0, 1, 0, -1]  # \인 경우 회전 방향
tmp = arr[kx][ky]

while in_range(kx, ky):
    if arr[kx][ky] == '/':  # left
        if tmp == '\\':
            move_dir = (move_dir + 1) % 4
        tmp = '/'
        move_dir = (3 - move_dir) % 4
        kx, ky = kx + left_x[move_dir], ky + left_y[move_dir]
        
    elif arr[kx][ky] == '\\':  # right
        if tmp == '/':
            move_dir = (move_dir + 3) % 4
        tmp = '\\'
        move_dir = (3 - move_dir) % 4
        kx, ky = kx + right_x[move_dir], ky + right_y[move_dir]

    cnt += 1

print(cnt)