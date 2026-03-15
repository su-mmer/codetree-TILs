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
        if meet[meet[i][j]][0] == 1 and arr_k[meet[i][j]] < k:
            meet[i][0] = 1
            arr_k[meet[i][j]] += 1

# for elem in meet:
#     for e in elem[:10]:
#         print(e, end=' ')
#     print()

for i in range(1, n+1):
    print(meet[i][0], end='')