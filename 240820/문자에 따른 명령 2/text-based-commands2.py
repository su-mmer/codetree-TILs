dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_head = 3
x, y = 0, 0

string = input()

for order in string:
    if order == "L":
        dir_head = (dir_head + 3) % 4
    elif order == "R":
        dir_head = (dir_head + 1) % 4
    elif order == "F":
        x, y = x + dx[dir_head], y + dy[dir_head]

print(x, y)