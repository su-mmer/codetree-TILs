n = int(input())

cnt = 1
for i in range(n):
    if i % 2 == 0:
        cnt = (i * n) + 1
        for j in range(n):
            print(cnt, end=' ')
            cnt += 1
    else:
        cnt = (i + 1) * n
        for j in range(n):
            print(cnt, end=' ')
            cnt -= 1
    print()