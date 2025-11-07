n = int(input())
arr = [ [0 for _ in range(n)] for _ in range(n) ]

# 배열 채우기
num = 1
for j in range(n):
    if j % 2 == 0:
        for i in range(n):
            arr[i][j] = num
            num += 1
    else:
        for i in range(n):
            arr[i][j] = num
            num += 1

# 배열 출력
for row in arr:
    for elem in row:
        print(elem, end=' ')
    print()