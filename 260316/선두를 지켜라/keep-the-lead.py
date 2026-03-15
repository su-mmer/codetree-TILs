n, m = map(int, input().split())
arr_a = [0 for _ in range(1000 * 1000)]
arr_b = [0 for _ in range(1000 * 1000)]

# A의 움직임 기록
time = 0
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        time += 1
        arr_a[time] = arr_a[time-1] + v

# B의 움직임 기록
time = 0
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        time += 1
        arr_b[time] = arr_b[time-1] + v

# 선두 비교
cnt = 0
for i in range(2, time):
    # print(arr_a[i], arr_b[i])
    if arr_a[i] < arr_b[i] and arr_a[i-1] >= arr_b[i-1]:
        cnt += 1
    elif arr_b[i] < arr_a[i] and arr_b[i-1] >= arr_a[i-1]:
        cnt += 1

print(cnt)
