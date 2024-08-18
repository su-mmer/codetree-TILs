n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
direction = ['E', 'S', 'W', 'N']
x, y = 0, 0  # 시작 위치

for _ in range(n):
    d, t = input().split()
    x, y = x + dx[direction.index(d)] * int(t), y + dy[direction.index(d)] * int(t)

print(x, y)