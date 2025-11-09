n, a = tuple(input().split())
n = int(n)

cnt = 0
for _ in range(n):
    string = input()
    if string == a:
        cnt += 1

print(cnt)