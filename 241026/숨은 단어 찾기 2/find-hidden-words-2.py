n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]

flag = False
cnt = 0  # count 'LEE'
for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            if j <= m-3 and arr[i][j+1] == 'E' and arr[i][j+2] == 'E':  # horizontal right
                cnt += 1
            if j >= 2 and arr[i][j-1] == 'E' and arr[i][j-2] == 'E':  # horizontal left
                cnt += 1
            if i <= n-3 and arr[i+1][j] == 'E' and arr[i+2][j] == 'E':  # vertical low
                cnt += 1
            if i >= 2 and arr[i-1][j] == 'E' and arr[i-2][j] == 'E':  # vertical high
                cnt += 1
            if i <= n-3 and j <= m-3 and arr[i+1][j+1] == 'E' and arr[i+2][j+2] == 'E':  # diagonal right low
                cnt += 1
            if i <= n-3 and j >= 2 and arr[i+1][j-1] == 'E' and arr[i+2][j-2] == 'E':  # diagonal left low
                cnt += 1
            if i >= 2 and j <= m-3 and arr[i-1][j+1] == 'E' and arr[i-2][j+2] == 'E':  # diagonal right high
                cnt += 1
            if i >=2 and j >= 2 and arr[i-1][j-1] == 'E' and arr[i-2][j-2] == 'E':  # diagonal left high
                cnt += 1
print(cnt)