r, c = map(int, input().split())
arr = [list(input().split()) for _ in range(r)]

cnt = 0
for i in range(1, r):
    for j in range(1, c):
        for n in range(i + 1, r - 1):
            for m in range(j + 1, c -1):
                if arr[0][0] != arr[i][j] and arr[i][j] != arr[n][m] and arr[n][m] != arr[r-1][c-1]:
                    cnt += 1

print(cnt)