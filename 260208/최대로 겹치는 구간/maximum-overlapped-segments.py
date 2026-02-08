n = int(input())
orders = [ list(map(int, input().split())) for _ in range(n) ]
blocks = [ 0 for _ in range(201) ]

for order in orders:
    for o in range(order[0], order[1]):
        blocks[o+100] += 1

    
print(max(blocks))