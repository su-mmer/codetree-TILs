n, m = map(int, input().split())
arr_a = [0 for _ in range(1000001)]
arr_b = [0 for _ in range(1000001)]

# A의 이동거리
time_a = 1
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(t):
        arr_a[time_a] = arr_a[time_a - 1] + v
        time_a += 1

# B의 이동거리
time_b = 1
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(t):
        arr_b[time_b] = arr_b[time_b - 1] + v
        time_b += 1

# 조합
count = 0
first = ''
# first = 'a' if arr_a[1] > arr_b[1] else 'b'
for i in range(2, time_a):
    if arr_a[i] == arr_b[i] and arr_a[i-1] != arr_b[i]:
        count += 1
        frist = 'ab'
    if arr_a[i-1] == arr_b[i-1] and arr_a[i] > arr_b[i]:
        count += 1
        first = 'a'
    if arr_a[i-1] == arr_b[i-1] and arr_a[i] < arr_b[i]:
        count += 1
        first = 'b'
    # if arr_a[i] <= arr_b[i] and arr_a[i-1] > arr_b[i-1]:
    #     first = 'b'
    #     count += 1
    # else:
    #     first = 'a'
    # if time_a[i] != time_a[i-1] or time_b[i] != time_b[i]:
        # count += 1
    # print(arr_a[i], arr_b[i])
print(count)