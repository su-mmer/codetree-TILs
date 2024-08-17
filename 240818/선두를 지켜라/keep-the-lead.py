n, m = map(int, input().split())
arr_a = []
arr_b = []

# A의 위치
p = 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(1, t + 1):
        arr_a.append(p + i * v)
    p += v * t

# B의 위치
p = 0
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(1, t + 1):
        arr_b.append(p + i * v)
    p += v * t

# 현재 선두 기록
top = []
for i in range(len(arr_a)):
    if arr_a[i] < arr_b[i]:
        top.append('b')
    elif arr_a[i] > arr_b[i]:
        top.append('a')
    else:  # 둘이 동일한 위치라면 건너뜀
        continue

# 선두가 변경된 횟수
count = 0
for i in range(1, len(top)):
    if top[i-1] != top[i]:
        count += 1

print(count)