n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n)]
length = len(arr)

max_cnt = 0
for i in range(length):
    for j in range(length - 2):
        max_cnt = max(max_cnt, arr[i][j] + arr[i][j+1] + arr[i][j+2])

print (max_cnt)