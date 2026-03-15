n, m, k = map(int, input().split())
penalty = [0 for _ in range(n+1)]

p = False
for _ in range(m):
    num = int(input())
    penalty[num] = penalty[num] + 1
    if penalty[num] == k:
        s = num
        p = True
        break

print(num) if p else print(-1)