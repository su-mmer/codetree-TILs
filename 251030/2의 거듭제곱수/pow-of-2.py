n = int(input())
tmp = 1
cnt = 0
while True:
    tmp *= 2
    cnt += 1
    if tmp == n:
        print(cnt)
        break