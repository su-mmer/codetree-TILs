orders = list(input())

dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]
move_dir = 2
nx, ny = 0, 0
time, tag = 0, False

for o in orders:
    if o == 'L':
        move_dir = (move_dir + 1) % 4 
    elif o == 'R':
        move_dir = (move_dir - 1) % 4
    elif o == 'F':
        nx, ny = nx + dxs[move_dir], ny + dys[move_dir]
    time += 1

    if nx == 0 and ny == 0:
        print(time)
        tag = True
        break

if tag == False:
    print(-1)