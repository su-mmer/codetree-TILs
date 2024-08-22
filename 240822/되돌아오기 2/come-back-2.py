orders = input()
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]  #  동남서북
dir_num = 3  # 북으로 시작
x, y = 0, 0  # 시작 위치

time = 0
flag = False
for order in orders:
    if order == 'F':
        x, y = x + dxs[dir_num], y + dys[dir_num]
    elif order == 'L': 
        dir_num = (dir_num + 3) % 4
    elif order == 'R':
        dir_num = (dir_num + 1) % 4
    
    time += 1
    
    if x == 0 and y == 0:
        flag = True
        break

print(time) if flag else print(-1)