n, m = map(int, input().split())
arr_a = [0 for _ in range(1000 * 1000 +1)]
arr_b = [0 for _ in range(1000 * 1000 +1)]

time_a = 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        time_a += 1
        arr_a[time_a] = arr_a[time_a-1] + v

time_b = 0
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        time_b += 1
        arr_b[time_b] = arr_b[time_b-1] + v

cnt = 0
for i in range(1, time_a+1):    
    if arr_a[i] == arr_b[i] and arr_a[i-1] == arr_b[i-1]:
        continue
    elif arr_a[i] > arr_b[i] and arr_a[i-1] > arr_b[i-1]:
        continue
    elif arr_a[i] < arr_b[i] and arr_a[i-1] < arr_b[i-1]:
        continue

    cnt += 1

print(cnt)
