r, c = map(int, input().split())
arr = [list(input().split()) for _ in range(r)]

# find_stack = []
cnt = 0
# c_point, r_point = 1, 1
# for i in range(1, c):
#     for j in range(1, r):
#         if arr[i][j] != block and cnt < 3:
#             find_stack.append([i, j, cnt])
#             # color = arr[i][j]
#             arr[i][j] = 'A'
#             print(arr)
#     cnt += 1

for i in range(1, c):
    for j in range(1, r):
        if arr[i][j] != arr[0][0]:
            for k in range(i+1, c):
                for l in range(j+1, r):
                    if arr[k][l] != arr[i][j]:
                        for g in range(k+1, c):
                            for t in range(l+1, c):
                                if arr[g][t] != arr[k][l]:
                                    cnt += 1
print(cnt)