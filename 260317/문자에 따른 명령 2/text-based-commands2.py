dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
order = input()

x, y = 0, 0
dir_num = 3
for o in order:
    if o == 'L':
        dir_num = (dir_num + 3) % 4
    elif o == 'R':
        dir_num = (dir_num + 1) % 4
    elif o == 'F':
        x, y = x + dx[dir_num], y + dy[dir_num]
    
print(x, y)