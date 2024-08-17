n, m = map(int, input().split())
arr_a = []
arr_b = []

p = 0
for _ in range(n):
    v, t = map(int, input().split())
    for i in range(1, t + 1):
        arr_a.append(p + i * v)
    p += v * t

p = 0
for _ in range(m):
    v, t = map(int, input().split())
    for i in range(1, t + 1):
        arr_b.append(p + i * v)
    p += v * t
# print(arr_a)
# print(arr_b)
# first = 'a' if arr_a[0] > arr_b[0] else 'b'
top = []
for i in range(len(arr_a)):
    if arr_a[i] < arr_b[i]:
        # first = 'b'
        top.append('b')
    elif arr_a[i] > arr_b[i]:
        top.append('a')
    else:
        continue

# print(top)
count = 0
for i in range(len(top)):
    if i == 0 or top[i-1] != top[i]:
        # print(i)
        count += 1

print(count-1)