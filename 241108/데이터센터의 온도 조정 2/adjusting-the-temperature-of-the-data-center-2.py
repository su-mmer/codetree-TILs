n, c, g, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

max_work = 0
for tem in range(1000):
# for a, b in arr:
    sum_work = 0
    for a, b in arr:
    # for tem in range(1000):
        if tem < a:
            work = c
        elif a <= tem and tem <= b:
            work = g
        elif b < tem:
            work = h
        sum_work += work
    max_work = max(max_work, sum_work)
    # sum_work += work

print(max_work)