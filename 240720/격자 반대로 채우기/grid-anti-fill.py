n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]
updown_flag = True
cnt = 1

for i in range(n-1, -1, -1):
    if updown_flag == True:
        for j in range(n-1, -1, -1):
            arr[j][i] = cnt
            cnt += 1
        updown_flag = False
    else:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1
        updown_flag = True

for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()