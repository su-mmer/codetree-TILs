import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_dim = sys.maxsize
for i in range(n):
    max_x, max_y = -sys.maxsize, -sys.maxsize  # init
    min_x, min_y = sys.maxsize, sys.maxsize  # init
    for j in range(n):
        if i == j:  # same pass
            continue
        max_x = max(max_x, arr[j][0])
        max_y = max(max_y, arr[j][1])
        min_x = min(min_x, arr[j][0])
        min_y = min(min_y, arr[j][1])
    # print(max_x, min_x, max_y, min_y)
    dimension = (max_x - min_x) * (max_y - min_y)  # rectangle dimension
    min_dim = min(min_dim, dimension)

print(min_dim)