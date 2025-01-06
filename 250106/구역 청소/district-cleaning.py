xa, xb = map(int, input().split())
xc, xd = map(int, input().split())
arr = [False] * 101
cnt = 0

for i in range(xa, xb):
    arr[i] = True
for i in range(xc, xd):
    arr[i] = True

for a in arr:
    if a:
        cnt += 1

print(cnt)