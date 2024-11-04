n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        if arr[i][0] <= arr[j][0] and arr[j][1] <= arr[i][1]:
            cnt += 1

print(n - cnt - 1)