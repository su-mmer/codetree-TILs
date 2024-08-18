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

count = 0  # 선두 변경 횟수
first = ''  # 선두 주자
for i in range(1, time_a):
    if arr_a[i] < arr_b[i] and first != 'b':
        first = 'b'
        count += 1
    elif arr_a[i] == arr_b[i] and first != 'ab':
        first = 'ab'
        count += 1
    elif arr_a[i] > arr_b[i] and first != 'a':
        first = 'a'
        count += 1

print(count)