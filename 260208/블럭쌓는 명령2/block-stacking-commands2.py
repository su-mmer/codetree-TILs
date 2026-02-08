n, k = map(int, input().split())
order = [ list(map(int, input().split())) for _ in range(k) ]

blocks = [ 0 for _ in range(n+1) ]
for o in order:
    for i in range(o[0], o[1]+1):
        blocks[i] += 1

print(max(blocks))