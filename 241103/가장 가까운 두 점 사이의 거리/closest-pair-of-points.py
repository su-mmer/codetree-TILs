import sys
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_square = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        x = (arr[i][0] - arr[j][0])
        y = (arr[i][1] - arr[j][1])
        square = x * x + y * y
        min_square = min(square, min_square)
    
print(min_square)