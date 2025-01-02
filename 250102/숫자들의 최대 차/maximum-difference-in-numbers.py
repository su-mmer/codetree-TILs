n, k = map(int, input().split())
arr = [ int(input()) for _ in range(n) ]
arr.sort()

max_cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        diff = arr[j] - arr[i]  # 원소의 차
        if diff <= k:
            cnt = 0
            for x in arr:
                if arr[i] <= x and x <= arr[j]:
                    cnt += 1
            if max_cnt <= cnt:
                max_cnt = cnt

print(max_cnt)