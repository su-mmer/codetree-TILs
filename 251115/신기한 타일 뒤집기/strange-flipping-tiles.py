n = int(input())
OFFSET = 100 * n
tiles = [ 0 for _ in range(OFFSET * 2 + 1) ]

pv = OFFSET  # 시작 위치
for _ in range(n):
    x, d = input().split()
    x = int(x)

    if d == "L":
        for i in range(pv, pv-x, -1):
            tiles[i] = "W"
        pv = pv - x + 1  # 마지막으로 뒤집은 타일 위치
    elif d == "R":
        for i in range(pv, pv+x):
            tiles[i] = "B"
        pv = pv + x - 1  # 마지막으로 뒤집은 타일 위치
    # print(tiles)

w, b = 0, 0
for c in tiles:
    if c == "W":
        w += 1
    elif c == "B":
        b += 1

print(w, b, end=' ')