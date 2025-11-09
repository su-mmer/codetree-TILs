a, b = map(int, input().split())

num = str(a + b)
cnt = 0
for c in num:
    if c == '1':
        cnt += 1

print(cnt)