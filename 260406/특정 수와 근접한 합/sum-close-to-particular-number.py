import sys
n, s =  map(int, input().split())
numbers = list(map(int, input().split()))

min_t = sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        t = 0
        for k in range(n):
            if k == i or k == j:  # 2개 제외
                continue
            t += numbers[k]  # 나머지 합
        t = abs(t - s)

        min_t = min(min_t, t)

print(min_t)