n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt1, cnt2 = 0, 0  # first mini board cnt, second mini board cnt
max_cnt = 0  # biggest cnt
for i in range(n-1):
    for j in range(n-2):
        cnt1 = arr[i][j] + arr[i][j+1] + arr[i][j+2]  # first mini board
        for m in range(j+3, n-2):  # 같은 줄 check
            cnt2 = arr[i][m] + arr[i][m+1] + arr[i][m+2]
            max_cnt = max(max_cnt, cnt1 + cnt2)
        for k in range(i+1, n):  # 아래 줄부터 check
            for l in range(n-2):
                cnt2 = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)