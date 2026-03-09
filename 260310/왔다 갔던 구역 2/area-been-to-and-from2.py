n = int(input())
block = [0 for _ in range(10*100*2+2)]  # total block init

p = 1000  # 위치
for _ in range(n):
    x, d = input().split()
    x = int(x)
    if d == 'R':  # x R 인 경우
        for i in range(p, p+x):
            block[i] += 1
        p += x
    elif d == 'L':  # x L인 경우
        for i in range(p-1, p-x-1, -1):
            block[i] += 1
        p -= x

cnt = 0  # 2 이상 총 개수
for i in block:
    if i >= 2:
        cnt += 1

print(cnt)