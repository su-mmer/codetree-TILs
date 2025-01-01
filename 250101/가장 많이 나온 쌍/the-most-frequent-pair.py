n, m = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(m)]

max_cnt = 0
for a, b in arr:
    count = 0
    for x, y in arr:
        if set([a, b]) == set([x, y]):
            count += 1
    max_cnt = max(max_cnt, count)

print(max_cnt)