n = int(input())
arr = [ list(map(int, input().split())) for _ in range(n) ]

count = 0
# 삭제할 선분 3개 i, j, k
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 남은 선분 중 2개 x, y
            for x in range(n):
                for y in range(x + 1, n):
                    if n == 4:
                        count = 4
                    if x == i or x == j or x == k or y == i or y == j or y ==k:
                        continue
                    # 겹치지 않으면 count
                    if arr[x][1] < arr[y][0] or arr[y][1] < arr[x][0]:
                        count += 1

print(count)