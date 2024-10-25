r, c = 19, 19
board = [list(map(int, input().split())) for _ in range(19)]

flag  = False  # 오목 성공 flag
find, color = 0, 0  # check할 color, 성공한 color
middle_r, middle_c = 0, 0  # 성공한 color의 좌표
for i in range(r):
    for j in range(c):
        if board[i][j] != 0:  # find black or white
            find = board[i][j]  # what color
            if j <= c - 5:  # 1. horizontal check
                flag = True
                for n in range(1, 5):
                    if board[i][j+n] != find:
                        flag = False
                        break
                if flag == True:
                    color = find
                    middle_r, middle_c = i, j+2
            if i <= c - 5:  # 2. vertical check
                flag = True
                for n in range(1, 5):
                    if board[i+n][j] != find:
                        flag = False
                        break
                if flag == True:
                    color = find
                    middle_r, middle_c = i+2, j
            if i <= c - 5 and j <= c - 5:  # 3. diagonal right check
                flag = True
                for n in range(1, 5):
                    if board[i+n][j+n] != find:
                        flag = False
                        break
                if flag == True:
                    color = find
                    middle_r, middle_c = i+2, j+2
            if i <= c - 5 and j >= 4:  # 3. diagonal left
                flag = True
                for n in range(1, 5):
                    if board[i+n][j-n] != find:
                        flag = False
                        break
                if flag == True:
                    color = find
                    middle_r, middle_c = i+2, j-2

# Print Answer
print(color)
if color == 1 or color == 2:
    print(middle_r + 1, middle_c + 1)