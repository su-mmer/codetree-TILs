n, k = map(int, input().split())
r = 200 + 100
arr = [0] * (r * 2 + 1)

for _ in range(n):
    candy, basket = map(int, input().split())
    arr[r + basket + 1] += candy

max_cnt = 0
for i in range(r + 1, r * 2 + 1 - k):  # c의 범위
    cnt = 0
    for j in range(i - k, i + k + 1):
        cnt += arr[j]

    max_cnt = max(max_cnt, cnt)

print(max_cnt)