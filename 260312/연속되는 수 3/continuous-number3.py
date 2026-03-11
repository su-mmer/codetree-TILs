n = int(input())
arr = [int(input()) for _ in range(n)]

cnt, ans = 0, 0  # 연속 수열 길이, 최대 길이
for i in range(n):
    if i >= 1 and arr[i] * arr[i-1] > 0:
        cnt += 1
    else:
        cnt = 1

    ans = max(ans, cnt)

print(ans)