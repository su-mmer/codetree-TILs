n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        for k in range(n):
            if k == i or k == j:
                continue
            x1, y1 = arr[i][0], arr[i][1]
            x2, y2 = arr[j][0], arr[j][1]
            x3, y3 = arr[k][0], arr[k][1]

            dimension = 0
            x_dimension, y_dimension = 0, 0
            if x1 == x2 or x2 == x3 or x3 == x1:
                max_x = max(max(x1, x2), x3)
                max_y = max(max(y1, y2), y3)
                min_x = min(min(x1, x2), x3)
                min_y = min(min(y1, y2), y3)
                x_dimension = (max_x - min_x) * (max_y - min_y)
            if y1 == y2 or y2 == y3 or y3 == y1:
                max_x = max(max(x1, x2), x3)
                max_y = max(max(y1, y2), y3)
                min_x = min(min(x1, x2), x3)
                min_y = min(min(y1, y2), y3)
                y_dimension = (max_x - min_x) * (max_y - min_y)
            max_dim = max(x_dimension, y_dimension)

print(max_dim)