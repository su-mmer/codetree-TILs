n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

max_abs, max_cnt = 0, 0
for i in range(n):
    for j in range(i + 1, n):
        diff = arr[j] - arr[i]
        if diff <= k and max_abs <= diff:
            cnt = 0
            for x in range(n):
                if arr[i] <= arr[x] and arr[x] <= arr[j]:
                    cnt += 1
            if max_cnt <= cnt:
                max_abs = diff
                max_cnt = cnt

print(max_cnt)