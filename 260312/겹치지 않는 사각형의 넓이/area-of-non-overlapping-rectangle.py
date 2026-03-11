OFFSET = 1000
blocks = [[False for _ in range(OFFSET * 2 + 1)] for _ in range(OFFSET * 2 + 1)]

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))
list_m = list(map(int, input().split()))

for i in list_a:
    i += OFFSET
for i in list_b:
    i += OFFSET
for i in list_m:
    i += OFFSET

for i in range(list_a[0], list_a[2]):
    for j in range(list_a[1], list_a[3]):
        blocks[i][j] = True

for i in range(list_b[0], list_b[2]):
    for j in range(list_b[1], list_b[3]):
        blocks[i][j] = True

for i in range(list_m[0], list_m[2]):
    for j in range(list_m[1], list_m[3]):
        blocks[i][j] = False

# 넓이 계산
cnt = 0
for elem in blocks:
    for e in elem:
        if e == True:
            cnt += 1

print(cnt)