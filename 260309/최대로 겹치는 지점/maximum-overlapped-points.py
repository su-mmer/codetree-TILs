n = int(input())
block = [0 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, y+1):
        block[i] += 1

print(max(block))