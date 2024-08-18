n, m = map(int, input().split())
arr_a=[0 for _ in range(1000001)]
arr_b=[0 for _ in range(1000001)]

# A가 움직인 위치
pos_a = 1
for _ in range(n):
    t, d = input().split()
    for _ in range(int(t)):
        arr_a[pos_a] = arr_a[pos_a - 1] + (1 if d == 'R' else -1)
        pos_a += 1

# B가 움직인 위치
pos_b = 1
for _ in range(m):
    t, d = input().split()
    for _ in range(int(t)):
        arr_b[pos_b] = arr_b[pos_b - 1] + (1 if d == 'R' else -1)
        pos_b += 1

# 먼저 멈춘 로봇의 위치는 그대로이므로 다른 로봇이 멈출때까지 마지막 위치로 채움
if pos_a >= pos_b:
    for i in range(pos_b, pos_a):
        arr_b[i] = arr_b[pos_b - 1]
else:
    for i in range(pos_a, pos_b):
        arr_a[i] = arr_a[pos_a - 1]

# 로봇 위치 비교
count = 0
for i in range(1, max(pos_a, pos_b)):
    if arr_a[i] == arr_b[i]:
        if arr_a[i - 1] != arr_b[i - 1]:
            count += 1
        else:
            continue

print(count)