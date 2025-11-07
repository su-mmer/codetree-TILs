n, m = map(int, input().split())
arr = [ [ 0 for _ in range(m) ] for _ in range(n) ]

num = 1
for j in range(m):
    for i in range(n):
        if j-i > -1:
            arr[i][j-i] = num
            num += 1

for i in range(1, n):
    for j in range(m-1, -1, -1):
        if i < n:
            arr[i][j] = num
            i += 1
            num += 1

# 배열 출력
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()