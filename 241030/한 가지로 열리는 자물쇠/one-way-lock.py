n = int(input())
a, b, c = map(int, input().split())

# 1~6 까지 중복해서 뽑아서 3자리 숫자를 만들어야 함
cnt = 0
for x in range(1, n+1):
    for y in range(1, n+1):
        for z in range(1, n+1):
            if abs(x-a) <= 2 or abs(y-b) <= 2 or abs(z-c) <= 2:
                cnt += 1

print(cnt)