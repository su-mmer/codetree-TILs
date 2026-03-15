n, k, p, t = map(int, input().split())
meet = [[0 for _ in range(250+1)] for _ in range(n+1)]
meet[p][0] = 1
arr_k = [0 for _ in range(n+1)]

for i in range(t):
    time, x, y = map(int, input().split())
    meet[x][time] = y
    meet[y][time] = x
    
for j in range(1, 251):
    for i in range(1, n+1):
        # print(meet[meet[i][j]][0])
        if meet[i][0] == 1 and arr_k[i] < k:  # 내가 감염자
            if meet[i][j] != 0 and meet[meet[i][j]][0] == 1:  # 상대 감염자
                arr_k[i] += 1  # 전염 횟수 +1
            if meet[i][j] != 0 and meet[meet[i][j]][0] == 0:  # 상대 미감염자
                arr_k[i] += 1  # 전염 횟수 +1
                meet[meet[i][j]][0] = 1
                # print("check: ", meet[i][j])
                break
        # print("me: ", i, " infect:", arr_k[i], " oth: ", meet[i][j], " othin: ", meet[meet[i][j]][0])

# for elem in meet:
#     for e in elem[:30]:
#         print(e, end=' ')
#     print()

for i in range(1, n+1):
    print(meet[i][0], end='')